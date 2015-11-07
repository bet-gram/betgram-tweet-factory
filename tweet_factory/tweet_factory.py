# all the imports
import sqlite3
import tweet_processing
from threading import Thread
from multiprocessing.pool import ThreadPool
from contextlib import closing
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

#Configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

#Little application :)
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.route('/')
def show_entries():
    cur = g.db.execute('select * from metrics order by retweet_count desc')
    entries = [dict(screen_name=row[0],follower_count=row[1],retweet_count=row[2],favorite_count=row[3]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)

if __name__ == '__main__':
    app.run()
    #thread = Thread(target = tweet_processing.tweet_processing)
    #thread.start()
    pool = ThreadPool(processes=1)
    async_result = pool.apply_async(tweet_processing.tweet_processing)
    screen_names = async_result.get()
    print screen_names

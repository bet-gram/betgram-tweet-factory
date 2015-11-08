# all the imports
import sqlite3
import tweet_processing
import flask
from threading import Thread
from multiprocessing.pool import ThreadPool
from contextlib import closing
from flask import Flask, jsonify, request, session, g, redirect, url_for, \
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
    entries = [dict(screen_name=row[0],follower_count=row[1],retweet_count=row[2],weighted_rt_index=row[3]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)

@app.route('/metrics')
def return_metrics():
        cur = g.db.execute('select * from metrics order by retweet_count desc')
        entries = [dict(screen_name=row[0],follower_count=row[1],retweet_count=row[2],weighted_rt_index=row[3]) for row in cur.fetchall()]
        return flask.jsonify(results=entries)

def add_entry(screen_name,follower_count,retweet_count):
    params = (screen_name,follower_count,retweet_count,1000000*retweet_count/(follower_count*tweet_processing.n_last_tweets))
    print params
    g.db.execute('insert into metrics values (?,?,?,?)', params)
    g.db.commit()

def app_run():
    app.run(use_reloader=False)

if __name__ == '__main__':
    thread = Thread(target = app_run)
    thread.start()
    #screen_names = tweet_processing.tweet_processing()
    #for squad, metrics in screen_names.iteritems():
        #with app.app_context():
            #g.db = connect_db()
            #add_entry(squad,metrics['follower_count'],metrics['retweet_count'])

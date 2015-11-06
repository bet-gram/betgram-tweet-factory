#Tweepy wrapper imports
import tweepy
from tweepy.auth import OAuthHandler

#Twitter API authentication fields
CONSUMER_KEY = "Bk2RrrGJIx3z3R3NzWXk2V0g0"
CONSUMER_SECRET = "Q5QPiTiapz1GewGV2aeLWoT8IoWXhjBFrC9bsQRvjOjpTSacPK"
TOKEN_KEY = "435217839-v08vYEBqddJQYHmH42ih269a6QsY0G4SozqEbs4P"
TOKEN_SECRET = "aYREePRSAlWpPyBQvs3VOYbHnt8w2UZCWyTj21yGzQGzW"

#This handles Twitter authetification and the connection to Twitter Streaming API
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(TOKEN_KEY, TOKEN_SECRET)
api = tweepy.API(auth)

#Squad list
squads = ["ManUtd","SwansOfficial","BurnleyOfficial","WBAFCofficial","whufc_official","LCFC","SpursOfficial","HullCity","CPFC","QPRFC","SouthamptonFC","stokecity","NUFC","Arsenal","SunderlandAFC","AVFCOfficial","ChelseaFC","LFC","Everton","MCFC"]

#Hash to store squads social information: followers, retweet_count and favorite_count for last 50 tweets
screen_names = {}

#Procedure to initialize hash values
def init_hash():
    for squad in squads:
        screen_names[squad] = {'follower_count':0,'retweet_count':0,'favorite_count':0}

def update_hash(screen_name):
    follower_count = 0
    retweet_count = 0
    favorite_count = 0
    tweets = api.user_timeline(screen_name = screen_name, count = 50)
    for tweet in tweets:
        retweet_count = retweet_count + tweet.retweet_count
        favorite_count = favorite_count + tweet.favorite_count
    screen_names[screen_name]['follower_count'] = follower_count
    screen_names[screen_name]['retweet_count'] = retweet_count
    screen_names[screen_name]['favorite_count'] = favorite_count

def tweet_processing():
    #Initialize hash
    init_hash()
    #Update hash
    for screen_name in screen_names.keys():
        update_hash(screen_name)
    print screen_names

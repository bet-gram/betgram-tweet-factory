#Tweepy wrapper imports
import tweepy
from tweepy.auth import OAuthHandler

#Twitter API authentication fields
CONSUMER_KEY = "Bk2RrrGJIx3z3R3NzWXk2V0g0"
CONSUMER_SECRET = "Q5QPiTiapz1GewGV2aeLWoT8IoWXhjBFrC9bsQRvjOjpTSacPK"
TOKEN_KEY = "435217839-v08vYEBqddJQYHmH42ih269a6QsY0G4SozqEbs4P"
TOKEN_SECRET = "aYREePRSAlWpPyBQvs3VOYbHnt8w2UZCWyTj21yGzQGzW"

#Hash to store squads social information
screen_names = {}

#Procedure to initialize hash values
def init_hash(init):
    screen_names["ManUtd"] = init
    screen_names["SwansOfficial"] = init
    screen_names["BurnleyOfficial"] = init
    screen_names["WBAFCofficial"] = init
    screen_names["whufc_official"] = init
    screen_names["LCFC"] = init
    screen_names["SpursOfficial"] = init
    screen_names["HullCity"] = init
    screen_names["CPFC"] = init
    screen_names["QPRFC"] = init
    screen_names["SouthamptonFC"] = init
    screen_names["stokecity"] = init
    screen_names["NUFC"] = init
    screen_names["Arsenal"] = init
    screen_names["SunderlandAFC"] = init
    screen_names["AVFCOfficial"] = init
    screen_names["ChelseaFC"] = init
    screen_names["LFC"] = init
    screen_names["Everton"] = init
    screen_names["MCFC"] = init

def update_hash(screen_name):
    tweets = api.user_timeline(screen_name = screen_name, count = 50)
    print screen_name
    for tweet in tweets:
        print tweet.retweet_count

if __name__ == '__main__':
    #This handles Twitter authetification and the connection to Twitter Streaming API
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(TOKEN_KEY, TOKEN_SECRET)
    api = tweepy.API(auth)
    #Initialize hash
    init_hash(0)
    #Update hash
    for screen_name in screen_names:
        update_hash(screen_name)

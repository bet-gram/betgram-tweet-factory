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
squads = ["ManUtd","SwansOfficial","afcbournemouth","WBAFCofficial","whufc_official","LCFC","SpursOfficial","NorwichCityFC","CPFC","WatfordFC","SouthamptonFC","stokecity","NUFC","Arsenal","SunderlandAFC","AVFCOfficial","ChelseaFC","LFC","Everton","MCFC"]

#Hash to store squads social information: followers, retweet_count and favorite_count for last 50 tweets
screen_names = {}

#Number of tweets to consider
n_last_tweets = 50

#Procedure to initialize hash values
def init_hash():
    for squad in squads:
        screen_names[squad] = {'follower_count':0,'retweet_count':0}

#Procedure to update hash values
def update_hash(screen_name):
    follower_count = 0
    retweet_count = 0
    user = api.get_user(screen_name = screen_name)
    follower_count = user.followers_count
    tweets = api.user_timeline(screen_name = screen_name, count = n_last_tweets)
    for tweet in tweets:
        retweet_count = retweet_count + tweet.retweet_count
    screen_names[screen_name]['follower_count'] = follower_count
    screen_names[screen_name]['retweet_count'] = retweet_count

#Translate screen_names to squad codes used throughout Betgram
def translate_screen_names(screen_names):
    squads_names = {}
    for screen_name in screen_names:
        if screen_name == squads[0]:
            new_key = "manchester_united"
        elif screen_name == squads[1]:
            new_key = "swansea"
        elif screen_name == squads[2]:
            new_key = "bournemouth"
        elif screen_name == squads[3]:
            new_key = "albion"
        elif screen_name == squads[4]:
            new_key = "westham"
        elif screen_name == squads[5]:
            new_key = "leicester"
        elif screen_name == squads[6]:
            new_key = "tottenham"
        elif screen_name == squads[7]:
            new_key = "norwich"
        elif screen_name == squads[8]:
            new_key = "crystal"
        elif screen_name == squads[9]:
            new_key = "watford"
        elif screen_name == squads[10]:
            new_key = "southampton"
        elif screen_name == squads[11]:
            new_key = "stoke"
        elif screen_name == squads[12]:
            new_key = "newcastle"
        elif screen_name == squads[13]:
            new_key = "arsenal"
        elif screen_name == squads[14]:
            new_key = "sunderland"
        elif screen_name == squads[15]:
            new_key = "aston_villa"
        elif screen_name == squads[16]:
            new_key = "chelsea"
        elif screen_name == squads[17]:
            new_key = "liverpool"
        elif screen_name == squads[18]:
            new_key = "everton"
        elif screen_name == squads[19]:
            new_key = "manchester_city"
        squads_names[new_key]=screen_names[screen_name]
    return squads_names

#Main procedure called by Flask app
def metric_processing():
    #Initialize hash
    init_hash()
    #Update hash
    for screen_name in screen_names.keys():
        update_hash(screen_name)
    return translate_screen_names(screen_names)

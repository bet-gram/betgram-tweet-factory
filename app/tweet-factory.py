#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import Cursor
from tweepy import API
import json

#Variables that contains the user credentials to access Twitter API 
access_token = "716680344-atp29IPuiLSiXR6vOHcEMk78tzXKDhy9uWMXm7Uy"
access_token_secret = "IIEmIHrhtrY5EGnpnx1zwQmipoT6u1bgCjjLFRT58wdvg"
consumer_key = "kHIJJ90oKRF6Svbf8UnYTRzrz"
consumer_secret = "zwc65T4hSA4lFk3eQSOp19BRCUvqtqNkOMx43xjX87X29hAkTs"

tweets = []


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def __init__(self):
        self.count = 0

    def on_data(self, data):
        if self.count == 10:
            return False
        try:
            self.count += 1         
            tweet = json.loads(data)
            place = tweet['text']
            if place:
                
                tweets.append(tweet)
            return True
        except:
            return True

        

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    api = API(auth)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['arsenal'])

    #l = Cursor(api.search, q='cricket', geocode="-22.9122,-43.2302,1km").items(10)

    #l = api.search(q="arsenal", geocode='51.5072,-0.1275,10000000km', count=100)
    #print l[-1]

    for tweet in tweets:
        print tweet['text']
        print 
        #print tweet['user']['time_zone']
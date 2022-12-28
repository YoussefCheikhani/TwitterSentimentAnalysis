from tweepy.streaming import Stream
from tweepy import OAuth2BearerHandler
from tweepy import API
from tweepy import Stream

import twitter_credentials

class StdOutListner(Stream):
    def on_data(self, data):
        print(data)
        return True
    
    def on_exception(self, exception):
        print(exception)
        return super().on_exception(exception)

if __name__ == "__main__":
    listner = StdOutListner(twitter_credentials.API_KEY, twitter_credentials.API_KEY_SECRET,twitter_credentials.ACCESS_TOKEN,twitter_credentials.ACCESS_TOKEN_SECRET)
    auth = OAuth2BearerHandler(twitter_credentials.BEARER_TOKEN)
    api = API(auth)

    #stream = Stream(twitter_credentials.API_KEY, twitter_credentials.API_KEY_SECRET,twitter_credentials.ACCESS_TOKEN,twitter_credentials.ACCESS_TOKEN_SECRET,listner)
    stream = Stream(twitter_credentials.API_KEY, twitter_credentials.API_KEY_SECRET,twitter_credentials.ACCESS_TOKEN,twitter_credentials.ACCESS_TOKEN_SECRET)
    stream.filter(track=["Tweepy"])

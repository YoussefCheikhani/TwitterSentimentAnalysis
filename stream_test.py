import tweepy
from tweepy import OAuth2BearerHandler
from tweepy import API
from tweepy import Stream

import twitter_credentials as tc

# authentication
auth = tweepy.OAuthHandler(tc.API_KEY, tc.API_KEY_SECRET)
auth.set_access_token(tc.ACCESS_TOKEN, tc.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
print(public_tweets[0].text)




#tc.API_KEY, tc.API_KEY_SECRET, tc.ACCESS_TOKEN, tc.ACCESS_TOKEN_SECRET
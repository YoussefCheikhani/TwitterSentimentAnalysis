import tweepy
from tweepy import OAuth2BearerHandler
from tweepy import API
from tweepy import Stream
import datetime

import twitter_credentials as tc

# authentication
auth = tweepy.OAuthHandler(tc.API_KEY, tc.API_KEY_SECRET)
auth.set_access_token(tc.ACCESS_TOKEN, tc.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

search_term = 'world cup 2022'
tweet_amount = 10

tweets = []
tmpTweets = tweepy.Cursor(method=api.search_tweets, q=search_term, lang='en',until="2022-12-23").items(tweet_amount)

for tweet in tmpTweets:
    print(tweet.created_at)


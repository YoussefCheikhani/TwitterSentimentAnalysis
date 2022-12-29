from textblob import TextBlob
import tweepy
import twitter_credentials as tc
import sys

#auth
auth = tweepy.OAuthHandler(tc.API_KEY, tc.API_KEY_SECRET)
auth.set_access_token(tc.ACCESS_TOKEN, tc.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

#printing tweets

search_term = 'world cup 2022'
tweet_amount = 200

tweets = tweepy.Cursor(method=api.search_tweets, q=search_term, lang='en').items(tweet_amount)

#for tweet in tweets:
    #print(tweet.text)

#Cleaning Tweets

polarity = 0

for tweet in tweets:
    tweet_text = tweet.text.replace('RT', '')       #Remove the RT Tags
    if tweet_text.startswith(' @'):                  #Remove usernames
        position = tweet_text.index(':')
        tweet_text = tweet_text[position+2:]
    if tweet_text.startswith('@'):                  #Remove usernames
        position = tweet_text.index(' ')
        tweet_text = tweet_text[position+2:]
    #print(tweet_text)
    #Analysis
    analysis = TextBlob(tweet_text)
    polarity += analysis.polarity

print(polarity)                            # We obtained A polarity of +54 which means the overal sentiment is very positive over the 200 tweets




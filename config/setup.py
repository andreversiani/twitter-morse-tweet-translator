import tweepy
from classes.user import User
from config.credentials import API_KEY, API_SECRET, API_TOKEN, API_TOKEN_SECRET, account_name

account_name = 'Madokera' #Account Name

def setup(name):
  auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
  auth.set_access_token(API_TOKEN, API_TOKEN_SECRET)
  api = tweepy.API(auth)
  user = User(name, api)
  return api, user

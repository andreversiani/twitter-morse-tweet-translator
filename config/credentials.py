import tweepy

def setup():
  API_KEY = ''  # API KEY
  API_SECRET = ''  # API secret key
  API_TOKEN = ''  # acess token
  API_TOKEN_SECRET = ''  # acess token secret

  auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
  auth.set_access_token(API_TOKEN, API_TOKEN_SECRET)
  api = tweepy.API(auth)
  return api

import tweepy

def setup():
  API_KEY = 'CwGZLsK1MXwrATXVPEt07e8P4'  # API KEY
  API_SECRET = 'UhxTiJRKtCUGz3N2niuoMgbw7DtSuftXUwgAAtHPcJUUYXz9iR'  # API secret key
  API_TOKEN = '1207941038549209088-yDciuvOYBwkhSv6jNSd9CATnBe2PlX'  # acess token
  API_TOKEN_SECRET = 'PjwbiOEJpB6K4AEa1Ynsvp78Wx1uxMFTIyDhbY6cIspH5'  # acess token secret

  auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
  auth.set_access_token(API_TOKEN, API_TOKEN_SECRET)
  api = tweepy.API(auth)
  return api

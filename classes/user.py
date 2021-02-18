import tweepy

class User:
  def __init__(self, user, api):
    self.api = api
    self.user = self.api.get_user(user)
    self.tweets = self.api.user_timeline(id=self.user.id, include_rts=False)
    self.last_tweet = self.tweets[0]
    self.prev_tweet = self.tweets[0]
  
  def update_last_tweet(self):
    self.tweets = self.api.user_timeline(id=self.user.id, include_rts=False)
    self.last_tweet = self.tweets[0]
  
  def update_prev_tweet(self):
    self.prev_tweet = self.tweets[0]
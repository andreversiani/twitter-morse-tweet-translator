from classes.tweet import Tweet

import time

def run(user, api):
  print("Bot is running")
  while True:
    user.update_last_tweet()
    if user.last_tweet.id != user.prev_tweet.id:
      print(f"New tweet detected. Text: {user.last_tweet.text}")
      tweet = user.last_tweet
      t = Tweet(tweet, user, api)
      t.handle_tweet()
      user.update_prev_tweet()
    time.sleep(30)
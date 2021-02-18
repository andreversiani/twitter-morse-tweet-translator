from classes.user import User

class Tweet:
  def __init__(self, tweet, user, api):
    self.user = user
    self.tweet = tweet
    self.tweet_text = tweet.text
    self.translated_text = ''
    self.api = api

  def has_media(self): 
    try:
        self.tweet.entities['media']
        return True
    except:
        return False
  
  def is_retweet(self):
    try:
        self.tweet.entities['urls'][0]['display_url'] 
        return True
    except:
        return False

  def https_erase(self):
    palavras = self.tweet_text.split()
    palavras.pop(-1)
    texto = ' '.join(palavras)
    return texto
  
  def lenght_fix(self):
    if len(self.tweet_text) > 280:
        while len(self.tweet_text) > 280:
            words = self.tweet_text.split()
            words.pop(-1)
            self.translated_text = ' '.join(words)
  
  def to_morse(self):
    morse = {'A': '.- ',     'B': '-... ',   'C': '-.-. ',
        'D': '-.. ',    'E': '. ',      'F': '..-. ',
        'G': '--. ',    'H': '.... ',   'I': '.. ',
        'J': '.--- ',   'K': '-.- ',    'L': '.-.. ',
        'M': '-- ',     'N': '-. ',     'O': '--- ',
        'P': '.--. ',   'Q': '--.- ',   'R': '.-. ',
     	  'S': '... ',    'T': '- ',      'U': '..- ',
        'V': '...- ',   'W': '.-- ',    'X': '-..- ',
        'Y': '-.-- ',   'Z': '--.. ',

        '0': '----- ',  '1': '.---- ',  '2': '..--- ',
        '3': '...-- ',  '4': '....- ',  '5': '..... ',
        '6': '-.... ',  '7': '--... ',  '8': '---.. ',
        '9': '----. ', ' ': '/ ', '.': '.-.-.- ',
        ',': '--..-- ', '?': '	..--.. ', '@':'.--.- ',
        '!' : '-.-.-- ', '/': '-..-. ', '(': '-.--. ',
        ')': '-.--.- ', ':': '---...', 'Á': '.- ', 'Â': '.- ',
        'Ã':'.- ', 'É': '. ', 'Ê': '. ', 'Ô': '--- ', 'Ó': '--- '
        }

    for letra in self.tweet_text:
        if letra.upper() in morse.keys():
            nova_letra = morse[letra.upper()]
        else:
            nova_letra = ''
        self.translated_text += nova_letra    
  
  def handle_tweet(self):
    tweet = Tweet(self.tweet, self.user, self.api)
    if tweet.has_media() or tweet.is_retweet():
      tweet.tweet_text = tweet.https_erase()
    if tweet.tweet_text:
      self.translated_text = tweet.to_morse()
      tweet.lenght_fix()
      try:
        self.api.update_status(status=f"Em morse: {tweet.translated_text}", in_reply_to_status_id=self.user.last_tweet.id, auto_populate_reply_metadata=True)
        print(f"New tweet posted. Text: {tweet.translated_text}")
      except:
        print("Error posting the tweet")

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey ='lfBOi9ywRgOnEZncpdYNbw'
csecret ='TR2XHLcHOzQL8PtwrdVMWhayeePLyNv4bDHry7HeL0'
atoken = '169505005-l7IoKI6PkjcwVsZPrcsrAGigRiwplztMREAt807d'
asecret = 'sgfXcgpH9rTJAMdrXzm2qsf1pmG7Pp5VvLY5cV5m9TAkb'
 
class listener(StreamListener):       
def on_data(self, data):
print data
return True
     
def on_error(self, status):
print status


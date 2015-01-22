from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json
from TwitterSentiment.test2 import tweets

 
ckey ='lfBOi9ywRgOnEZncpdYNbw'
csecret ='TR2XHLcHOzQL8PtwrdVMWhayeePLyNv4bDHry7HeL0'
atoken = '169505005-l7IoKI6PkjcwVsZPrcsrAGigRiwplztMREAt807d'
asecret = 'sgfXcgpH9rTJAMdrXzm2qsf1pmG7Pp5VvLY5cV5m9TAkb'

file = 'AlfamTwitterTraining.json'

tweets=[]
 
class listener(StreamListener):

    def on_data(self, data):
        try:  
            #print data
                   
            #tweet = data.split(',"text":"')[1].split('","source')[0]
            tweet = json.loads(data)
            print tweet["id"]
            
            saveFile = open(file,'a')
            saveFile.write(json.dumps(tweet))
            saveFile.write('\n')
            saveFile.close()
            return True
        except BaseException, e:
            print 'failed on_date,', str(e)
            time.sleep(5)
                
    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["geld lenen","lening","Defam","Credifance","Alpha Credit","Advanced Finance"
                            ,"krediet","private lease","Ing","Rabobank","Interbank","Nationale Nerderlanden"
                            ,"DGA","Geldshop","Geldlenen"])
#twitterStream.filter(track=["car"])
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json
from pymongo import MongoClient

#Mongo Settings
client = MongoClient()
db = client.Sentiment
Tweets = db.Tweet

#Twitter Credentials
ckey ='lfBOi9ywRgOnEZncpdYNbw'
csecret ='TR2XHLcHOzQL8PtwrdVMWhayeePLyNv4bDHry7HeL0'
atoken = '169505005-l7IoKI6PkjcwVsZPrcsrAGigRiwplztMREAt807d'
asecret = 'sgfXcgpH9rTJAMdrXzm2qsf1pmG7Pp5VvLY5cV5m9TAkb'

class listener(StreamListener):

    def on_data(self, data):
        try:  
                          
            tweet = json.loads(data)
            
            if tweet["lang"] == "nl":
                print tweet["id"]
                Tweets.insert(tweet)
            
            

            return True
        except BaseException, e:
            print 'failed on_date,', str(e)
            time.sleep(5)
                
    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter( track=["geld lenen"
                            ,"lening"
                            ,"Defam"
                            ,"DEFAM"
                            ,"Credivance"
                            ,"CREDIVANCE"
                            ,"Alpha Credit"
                            ,"ALPHA CREDIT"
                            ,"Advanced Finance"
                            ,"krediet"
                            ,"KREDIET"
                            ,"private lease"
                            ,"ing"
                            ,"Rabobank"
                            ,"Interbank"
                            ,"Nationale Nerderlanden"
                            ,"Geldshop"
                            ,"Geldlenen"
                            ,"ABN AMBRO"
                            ,"Independer"
                            ,"DGA adviseur"
                            ,"VDZ"
                            ,"vdz"
                            ,"Financieel Attent"
                            ,"Anderslenen"
                            ,"De Nederlandse Kredietmaatschappij"
                            ,"Moneycare"
                            ,"De Financiele Makelaar Kredieten"
                            ,"Finanplaza"
                            ,"Krediet"
                            ,"CFSN Kredietendesk"
                            ,"De Graaf Assurantien en Financieel Adviseurs"
                            ,"AMBTENARENLENING"
                            ,"VDZ Geldzaken"
                            ,"Financium Primae"
                            ,"SNS"
                            ,"AlfamConsumerCredit"
                            ,"GreenLoans"
                            ], languages="nl" 
                     )


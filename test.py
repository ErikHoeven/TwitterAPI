import pymongo
import nltk
import json
from json import JSONEncoder
from pymongo import MongoClient
from bson.objectid import ObjectId

#Variable declaratie
strSearchArg = "_id"


#TAG_TEKST
def tagText(tekst):
    
    tag = "neutraal"
    lstRules = {"vacature"              : 1.0
                ,"cybercriminelen"      :-1.0
                ,"fraude"               :-1.0
                ,"mooi"                 : 1.0
                ,"succes"               : 1.0
                ,"lid worden"           : 1.0
                ,"festival"             : 1.0
                ,"graag"                : 1.0
                ,"starten"              : 1.0
                ,"werk samen"           : 1.0
                ,"graag"                : 1.0
                ,"events"               : 1.0
                ,"aflossen"             : 1.0
                ,"clubkas campagne"     : 1.0
                ,"zoek accountmanager"  : 1.0
                ,"netwerken"            : 1.0
                ,"trainees"             : 1.0
                ,"zoek"                 : 1.0
                ,"steunt"               : 1.0
                ,"witwassen"            :-1.0
                ,"schadelijk"           :-1.0
                ,"boete"                :-1.0
                ,"inbraak"              :-1.0
                ,"Neen"                 :-1.0
                ,"opeens"               :-1.0
                ,"niks"                 :-1.0
                ,"phising"              :-1.0
                ,"failiet"              :-1.0
                ,"niet fair"            :-1.0
                ,"staking"              :-1.0
                ,"mag niet"             :-1.0
                ,"bankencrissis"        :-1.0
                ,"was het maar waar!"   :-1.0
                ,"witwassen"            :-1.0
                ,"korting"              : 1.0
                }
    
    score = 0.0
    
    for r in lstRules:
        if r in tekst.lower():
          #print lstRules[r]
          score = score + lstRules[r]
        
    if score > 0.0:
        tag = "goed"
    elif score < 0:
        tag = "slecht" 
    
    resltaat = "{\"tekst\":" + tekst +  ", \"sentiment\":" +  tag  +" }"
    return resltaat



#JSON Encoder
class MongoEncoder(JSONEncoder):
    def default(self, obj, **kwargs):
        if isinstance(obj, ObjectId):
            return str(obj)
        else:            
            return JSONEncoder.default(obj, **kwargs)


#Mongo Settings
client = MongoClient()
db = client.Sentiment
Tweets = db.Tweet
TweetTraining = db.TweetTraining

#GET TEXT_TAG FROM TWEET
for tweet in Tweets.find({"lang":"nl"},{"text"}).limit(50):
  
  strTweet = json.dumps(tweet, cls=MongoEncoder)
  tweetTekst = strTweet[9:strTweet.find(strSearchArg)-3]
  
  tagText(tweetTekst)
  
  #jsonTraingTweet = tagText(tweetTekst)
  #TweetTraining.insert(json.loads(jsonTraingTweet))
  
  

 
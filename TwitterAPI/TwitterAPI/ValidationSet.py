import pymongo
import nltk
import json
from json import JSONEncoder
from pymongo import MongoClient
from bson.objectid import ObjectId

#Variable declaratie
strSearchArg = "_id"


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
TweetValidation = db.TweetValidation

#GET TEXT_TAG FROM TWEET
for tweet in Tweets.find({"lang":"nl"},{"text"}).limit(250):
  
  strTweet = json.dumps(tweet, cls=MongoEncoder)
  tweetTekst = strTweet[9:strTweet.find(strSearchArg)-3]
  
  jsonTraingTweet = "{\"tekst\":" + tweetTekst +  ", \"sentiment\": \"goed\" }"
  TweetValidation.insert(json.loads(jsonTraingTweet))
  
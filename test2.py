import pymongo
import nltk
import json
from json import JSONEncoder
from pymongo import MongoClient
from bson.objectid import ObjectId
     
#Variable declaratie
strSearchArg = "_id"
i = 1


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


#Loop through tweets
lstTweets = []

for tweet in TweetTraining.find():
     strTekst = json.dumps(tweet["tekst"])
     strSentiment =  json.dumps(tweet["sentiment"])
     lstTweets[i] = [ strTekst , strSentiment ]
     #i = i + 1


#print lstTweets[2]


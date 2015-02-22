from TrainerScore import tagText
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
TweetTraining = db.TweetTraining

#GET PROPERTIES FROM TWEET
for tweet in Tweets.find({"lang":"nl"},{"text","geo","created_at","user.friends_count","user.name","user.followers_count","lang"}).limit(3000):
  
  try:
   
    lsTweet = tagText(tweet['text']
                                , tweet["user"]['name']
                                , tweet["user"]['friends_count']
                                , tweet["user"]['followers_count']
                                , tweet['geo']
                                , tweet['created_at']
                                , tweet['lang'])  
    
    TweetTraining.insert(lsTweet)
    
  except IOError as e:
      print "I/O error({0}): {1}".format(e.errno, e.strerror)
    

 
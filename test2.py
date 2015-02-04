import pymongo
import nltk
import json
from json import JSONEncoder
from pymongo import MongoClient
from bson.objectid import ObjectId
from nltk.corpus import words
from Crypto.Util.RFC1751 import wordlist
     
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
     strTekst = json.dumps(tweet["tekst"]).replace("\"", "")
     strSentiment =  json.dumps(tweet["sentiment"]).replace("\"", "")
     lstTweets.append([strTekst,strSentiment])


#For each tweet loop throught the words and set the words in a list
lst2Tweets = []
for (words, sentiment) in lstTweets:
     word_filtered = [e.lower() for e in words.split() if len(e) >= 3]
     lst2Tweets.append((word_filtered, sentiment))
      
def get_words_in_tweets(lst2Tweets):
     all_words = []
     for (words,sentiment) in lst2Tweets:
         all_words.extend(words)
     return all_words
 
def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features =  wordlist.keys()
    return word_features

word_features = get_word_features(get_words_in_tweets(lst2Tweets))


            
def extract_features (document):
     documents_word = set(document) 
     features = {}
     for word in word_features:
         features['contains(%s)' % word] = ( word in documents_word )
     return features
 
trainings_set = nltk.classify.apply_features(extract_features, lst2Tweets)
#print trainings_set
classifier = nltk.NaiveBayesClassifier.train(trainings_set)

print classifier.show_most_informative_features(32)



#print classifier.show_most_informative_features(32)

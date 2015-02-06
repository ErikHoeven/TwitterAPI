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
    lstRules = {"vacature"                          : 1.0
                ,"cybercriminelen"                  :-2.0
                ,"interesant"                       : 1.0
                ,"fraude"                           :-1.0
                ,"mooi"                             : 1.0
                ,"succes"                           : 1.0
                ,"lid worden"                       : 1.0
                ,"festival"                         : 1.0
                ,"graag"                            : 1.0
                ,"starten"                          : 1.0
                ,"werk samen"                       : 1.0
                ,"graag"                            : 1.0
                ,"events"                           : 1.0
                ,"aflossen"                         : 1.0
                ,"clubkas campagne"                 : 1.0
                ,"zoek accountmanager"              : 1.0
                ,"netwerken"                        : 1.0
                ,"trainees"                         : 1.0
                ,"zoek"                             : 1.0
                ,"steunt"                           : 1.0
                ,"witwassen"                        :-1.0
                ,"schadelijk"                       :-1.0
                ,"boete"                            :-1.0
                ,"inbraak"                          :-1.0
                ,"Neen"                             :-1.0
                ,"opeens"                           :-1.0
                ,"niks"                             :-1.0
                ,"phishing"                         :-2.0
                ,"failliet"                         :-1.0
                ,"niet fair"                        :-1.0
                ,"staking"                          :-1.0
                ,"mag niet"                         :-1.0
                ,"bankencrissis"                    :-2.0
                ,"was het maar waar!"               :-1.0
                ,"witwassen"                        :-3.0
                ,"korting"                          : 1.0
                ,":-)"                              : 2.0
                ,";-)"                              : 2.0
                ,";)"                               : 2.0
                ,":("                               :-2.0
                ,";-("                              :-2.0
                ,":-("                              :-2.0
                ,":("                               :-2.0
                ,";("                               :-2.0
                ,"favoriete"                        : 1.0
                ,"denkt met ons mee"                : 1.0
                , "geen gehoor gekregen"            :-1.0
                ,"geschreven voor klantenservice"   :-1.0
                ,"phishers"                         :-1.0
                }
    
    score = 0.0
    
    for r in lstRules:
        if r in tekst.lower():
          #print lstRules[r]
          score = score + lstRules[r]
        
    if score > 0.0:
        tag = "positief"
    elif score < 0:
        tag = "negatief" 
    
    
    resltaat = "{\"tekst\":" + tekst +  ", \"sentiment\":\""  +  tag  +"\" , \"score\":\""  +  str(score)  + "\", \"Categorie\":\""  +  tagCategorie(tekst)  +"\"}"
    return resltaat

def tagCategorie(tekst):
        categorie = "neutraal"
        
        lstCategorie = { "ing"                   :"Ing"
                        ,"#ing"                  :"Ing"
                        ,"@ing"                  :"Ing"
                        ,"rabobank"              :"Rabobank"
                        ,"rabo"                  :"Rabobank"
                        ,"#rabobank"             :"Rabobank"
                        ,"@rabobank"             :"Rabobank"
                        ,"@rabo"                 :"Rabobank"
                    }
        
        for r in lstCategorie:
             if r in   tekst.lower():
              categorie = lstCategorie[r] 
    
        return categorie

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
for tweet in Tweets.find({"lang":"nl"},{"text"}).limit(150):
  
  strTweet = json.dumps(tweet, cls=MongoEncoder)
  tweetTekst = strTweet[9:strTweet.find(strSearchArg)-3]
  
#print tagText(tweetTekst)
  
  jsonTraingTweet = tagText(tweetTekst) 
  try:
       
      TweetTraining.insert(json.loads(jsonTraingTweet))
  
  except:
      print jsonTraingTweet
    

 
import pymongo
import nltk
import json
from json import JSONEncoder
from pymongo import MongoClient
from bson.objectid import ObjectId

#Variable declaratie
strSearchArg = "_id"


#TAG_TEKST
def tagText(tekst,user,friends,follower,geo,creation_date,lang):
    
    tag = "neutraal"
    lstRules = {"vacature"                          : 1.0
                ,"cybercriminelen"                  :-2.0
                ,"interessant"                      : 1.0
                ,"fraude"                           :-2.0
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
                ,"neen"                             :-1.0
                ,"opeens"                           :-1.0
                ,"niks"                             :-1.0
                ,"phishing"                         :-2.0
                ,"failliet"                         :-1.0
                ,"niet fair"                        :-1.0
                ,"staking"                          :-1.0
                ,"mag niet"                         :-1.0
                ,"bankencrissis"                    :-2.0
                ,"#bankencrisis"                    :-2.0
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
                ,":)"                               : 2.0
                ,"tx"                               : 3.0
                ,"favoriete"                        : 1.0
                ,"denkt met ons mee"                : 1.0
                , "geen gehoor gekregen"            :-1.0
                ,"geschreven voor klantenservice"   :-1.0
                ,"phishers"                         :-1.0
                ,"gaat ook nergens over"            :-1.0
                ,"F***ing"                          :-2.0
                ,"ik mag niet"                      :-1.0
                ,"prutsers"                         :-2.0
                ,"jammer"                           :-1.0
                ,"starten"                          : 1.0
                ,"woningmarkt"                      : 1.0
                ,"f***ing"                          :-2.0
                ,"f*****g"                          :-2.0
                ,"f**k"                             :-2.0
                ,"extra"                            : 1.0
                ,"niet vooruit"                     :-1.0
                ,"benieuwd"                         : 1.0
                ,"foutmelding"                      :-1.0
                ,"storing"                          :-1.0
                ,"klanten geinformeerd"             : 2.0
                ,"gelukt"                           : 1.0
                ,"geen betalingen"                  :-2.0
                ,"dankjewel"                        : 2.0
                ,"kennismaking"                     : 1.0
                ,"te moeilijke mensen"              :-2.0
                ,"bespaar"                          : 1.0
                ,"maar"                             :-0.5
                ,"belachelijk"                      :-2.0
                ,"gezond"                           : 1.0
                ,"al"                               : 1.0
                ,"gefund"                           : 1.0
                ,"officieel"                        : 1.0
                  }
    
    score = 0.0
    colour = "blue"
    
    for r in lstRules:
        if r in tekst.lower():
          #print lstRules[r]
          score = score + lstRules[r]
        
    if score > 0.0:
        tag = "positief"
        colour = "green"
    elif score < 0:
        tag = "negatief"
        colour = "red" 
    
    
    
    resltaat  = { "tekst"        : tekst
                ,"username"      : user
                ,"friends"       : str(friends)
                ,"followers"     : str(follower)
                ,"locatie"       : geo
                ,"creation_date" : creation_date
                ,"tag"           : tag
                ,"categorie"     : tagCategorie(tekst)
                ,"score"         : str(score) 
                ,"lang"          : lang
                ,"colour"        : colour
               }

    return resltaat

def tagCategorie(tekst):
        categorie = "neutraal"
        
        lstCategorie = { "#ing"                                 :"Ing"
                        ,"@ing"                                 :"Ing"
                        ,"ING"                                  :"Ing"
                        ," ING "                                :"Ing"
                        ,"rabobank"                             :"Rabobank"
                        ,"rabo"                                 :"Rabobank"
                        ,"#rabobank"                            :"Rabobank"
                        ,"@rabobank"                            :"Rabobank"
                        ,"@rabo"                                :"Rabobank"
                        ,"ABN AMBRO"                            :"ABN AMBRO"
                        ,"SNS"                                  :"SNS Bank"
                        ,"#krediet"                             :"Krediet algemeen"
                        ,"#herfinanciering"                     :"Krediet algemeen"
                        ,"lening"                               :"Lening algemeen"
                        ,"hypotheek"                            :"hypotheek"  
                        ,"Independer"                           : "Distributie Partner" 
                        ,"DGA adviseur"                         : "Distributie Partner"
                        ,"VDZ"                                  : "Distributie Partner"
                         ,"vdz"                                 : "Distributie Partner"
                         ,"Financieel Attent"                   : "Distributie Partner"
                         ,"Anderslenen"                         : "Distributie Partner"
                         ,"De Nederlandse Kredietmaatschappij"  : "Distributie Partner"
                         ,"Moneycare"                           : "Distributie Partner"
                         ,"De Financiele Makelaar Kredieten"    : "Distributie Partner"
                         ,"Finanplaza"                          : "Distributie Partner"
                         ,"Krediet"                             : "Distributie Partner"
                         ,"CFSN Kredietendesk"                  : "Distributie Partner"
                         ,"De Graaf Assurantien en Financieel Adviseurs" : "Distributie Partner"
                         ,"AMBTENARENLENING"                    : "Distributie Partner"
                         ,"VDZ Geldzaken"                       : "Distributie Partner"
                         ,"Financium Primae"                    : "Distributie Partner"
        
        
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

#GET PROPERTIES FROM TWEET
for tweet in Tweets.find({"lang":"nl"},{"text","geo","created_at","user.friends_count","user.name","user.followers_count","lang"}).limit(3000):
  
  try:
       
#    print "--------tweet----------------"
    
    lsTweet = tagText(tweet['text']
                                , tweet["user"]['name']
                                , tweet["user"]['friends_count']
                                , tweet["user"]['followers_count']
                                , tweet['geo']
                                , tweet['created_at']
                                , tweet['lang'])  
    
    TweetTraining.insert(lsTweet)
    #print "-------- einde tweet----------------"
    
  
  except IOError as e:
      print "I/O error({0}): {1}".format(e.errno, e.strerror)
    

 
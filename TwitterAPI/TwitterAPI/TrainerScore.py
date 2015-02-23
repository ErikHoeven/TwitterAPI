'''
Created on Feb 22, 2015

@author: erik
'''

from TaggerCategorie import tagCategorie


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
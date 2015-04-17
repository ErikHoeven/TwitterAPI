'''
Created on Feb 22, 2015

@author: erik
'''
def tagCategorie(tekst):
        categorie = "neutraal"
        
        lstCategorie = { "#ing"                                 : "Ing"
                        ,"@ing"                                 : "Ing"
                        ,"ING"                                  : "Ing"
                        ," ING "                                : "Ing"
                        ,"rabobank"                             : "Rabobank"
                        ,"rabo"                                 : "Rabobank"
                        ,"#rabobank"                            : "Rabobank"
                        ,"@rabobank"                            : "Rabobank"
                        ,"@rabo"                                : "Rabobank"
                        ,"abn ambro"                            : "ABN AMBRO"
                        ,"sns"                                  : "SNS Bank"
                        ,"sns- bank"                            : "SNS Bank"
                        ,"dnb"                                  : "De Nederlandse Bank" 
                        ,"#krediet"                             : "Krediet algemeen"
                        ,"krediet"                              : "Krediet algemeen"
                        ,"#herfinanciering"                     : "Krediet algemeen"
                        ,"lening"                               : "Lening algemeen"
                        ,"minilening"                           : "Lening algemeen"
                        ,"flitslening"                         : "Lening algemeen"
                        ,"hypotheek"                            : "hypotheek" 
                        ,"hypothecair"                          : "hypotheek"
                        ,"independer"                           : "Distributie Partner" 
                        ,"dga adviseur"                         : "Distributie Partner"
                        ,"vdz"                                  : "Distributie Partner"
                         ,"Financieel attent"                   : "Distributie Partner"
                         ,"anderslenen"                         : "Distributie Partner"
                         ,"de nederlandse kredietmaatschappij"  : "Distributie Partner"
                         ,"moneycare"                           : "Distributie Partner"
                         ,"de Financiele Makelaar Kredieten"    : "Distributie Partner"
                         ,"Finanplaza"                          : "Distributie Partner"
                         ,"Krediet"                             : "Distributie Partner"
                         ,"CFSN Kredietendesk"                  : "Distributie Partner"
                         ,"De Graaf Assurantien en Financieel Adviseurs" : "Distributie Partner"
                         ,"AMBTENARENLENING"                    : "Distributie Partner"
                         ,"VDZ Geldzaken"                       : "Distributie Partner"
                         ,"Financium Primae"                    : "Distributie Partner"

        }
        
        
        for r in lstCategorie:
            if r.lower() in tekst.lower():
                categorie = lstCategorie[r] 
    
        return categorie

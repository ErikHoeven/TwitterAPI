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
                        ,"ABN AMBRO"                            : "ABN AMBRO"
                        ,"SNS"                                  : "SNS Bank"
                        ,"SNS."                                 : "SNS Bank"    
                        ,"sns- bank"                            : "SNS Bank"
                        ,"DNB"                                  : "De Nederlandse Bank" 
                        ,"DNB:"                                 : "De Nederlandse Bank"
                        ,"#krediet"                             : "Krediet algemeen"
                        ,"krediet"                              : "Krediet algemeen"
                        ,"#herfinanciering"                     : "Krediet algemeen"
                        ,"lening"                               : "Lening algemeen"
                        ,"hypotheek"                            : "hypotheek" 
                        ,"Hypothecair Krediet"                  : "hypotheek"
                        ," Hypothecair "                        : "hypotheek"
                        ,"Independer"                           : "Distributie Partner" 
                        ," Independer "                         : "Distributie Partner" 
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

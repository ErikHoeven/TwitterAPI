# -*- coding: utf-8 -*-

import nltk

def fltrStopWoorden(tekst): 
    
    
    tokens  = nltk.word_tokenize(tekst) 
    lsWords = [] 
    strWord = ""
    check = 0
    
    lsStopwoorden = [ "aan","afd","dat","de","den","der","des","deze","die","dit","dl","door","dr","ed","een","enige"
                     , "enkele","enz","etc","haar","het","hierin","hoe","hun","ik","inzake","is","je","na","hét"
                    ]

    for wordInToken in tokens:
        for wordInStopList in lsStopwoorden:
            if wordInToken.lower() != wordInStopList:
                #print wordInToken.lower() + " " + wordInStopList
                strWord =  wordInToken.lower()
            
            if wordInToken.lower() == wordInStopList:
                check = 1
        
         
        if check == 0: 
            lsWords.append(strWord)
        
        if check == 1:
            check = 0
     
      
    return (lsWords)

def fltrBijWoorden (lsWoorden):
    
    lsWords = [] 
    strWord = ""
    check = 0
     
    lsBijWoorden =  ["aan", "aaneen" , "aanstonds" , "aanvankelijk" , "absoluut" , "achter" , "achteraan" 
                     , "achteraf" , "achtereen" , "achtereenvolgens" , "achterin" , "achterna" , "achterom" 
                     , "achterop" , "achterover" , "achterstevoren" , "achteruit" , "achterwaarts" 
                     , "achterwege" , "acuut" , "af" , "afgezien" , "al" , "aldoor" , "aldus" , "allang" 
                     , "alleen" , "allengs" , "allereerst" , "allerminst" , "allesbehalve" , "alleszins" 
                     , "allicht" , "alom" , "alsmaar" , "alsmede" , "alsnog" , "althans" , "altijd" , "alvast" 
                     , "alweer" , "ambtshalve" , "amper" , "anders" , "andersom" , "anderszins" , "anderzijds" 
                     , "bar" , "beetje" , "beneden" , "bepaald" , "beslist" , "best" , "betrekkelijk" 
                     , "beurtelings" , "bij" , "bijeen" , "bijna" , "bijster" , "bijtijds" , "bijvoorbeeld" 
                     , "binnen" , "binnenkort" , "binnensmonds" , "binnenstebuiten" , "blijkbaar" , "blindelings" 
                     , "boven" , "bovenaan" , "bovendien" , "bovenop" , "breeduit" , "buiten" , "buitenshuis" 
                     , "circa" , "constant" , "contra" , "daar" , "daaraan" , "daarbij" , "daardoor" 
                     , "daarentegen" , "daarin" , "daarmee" , "daarna" , "daarnaast" , "daarom" , "daarop" 
                     , "daarover" , "daartoe" , "daaruit" , "daarvan" , "daarvoor" , "dadelijk" , "dan" , "danig" 
                     , "deels" , "derhalve" , "dermate" , "desalniettemin" , "desgewenst" , "desnoods" , "desondanks" 
                     , "destijds" , "dichterbij" , "dientengevolge" , "dikwijls" , "direct" , "ditmaal" , "domweg" 
                     , "doodstil"  , "doorgaans" , "echter" , "eenmaal" , "eens" , "eensklaps" , "eenvoudig" , "eerdaags" , "eerder" 
                     , "eergisteren" , "eerst" , "eindelijk" , "elders" , "enerzijds" , "enigszins" , "enkel" 
                     , "enorm" , "enzovoort" , "er" , "eraan" , "erbij" , "erg" , "ergens" , "erin" , "ermee" , "ernaar" 
                     , "erop" , "erover" , "eruit" , "ervan" , "ervandoor" , "ervoor" , "etcetera" , "eveneens" 
                     , "evengoed" , "evenmin" , "eventjes" , "evenwel" , "fijntjes" , "gaarne" , "gauw" 
                     , "gedeeltelijk" , "gedurende" , "geenszins" , "geheel" , "gelijk" , "gemakshalve" , "gemiddeld" 
                     , "gerust" , "gestaag" , "geweldig" , "gewoon" , "gewoonlijk" , "gewoonweg" , "gezamenlijk" 
                     , "ginder" , "ginds" , "gisteren" , "glad" , "gloeiend" ,"goed", "graag" , "grandioos", "grotendeels"
                     , "haast" , "halverwege" , "hard" , "hardop" , "hartstikke" , "heden" , "heel" , "heen" , "helaas" 
                     , "helemaal" , "her" , "herhaaldelijk" , "hier" , "hierbij" , "hierdoor" , "hierover" , "hoe" 
                     , "hoegenaamd" , "hoeverre" , "hogerop" , "hoofdzakelijk" , "hoogst", "hoogstens" , "iets" 
                     , "ietwat" , "ijlings" , "immer" , "immers" , "in" , "inclusief" , "inderdaad" , "indertijd" 
                     , "ineen" , "ineens" , "inmiddels" , "innerlijk" , "integendeel" , "intussen" , "ja" , "juist" 
                     , "kennelijk" , "klakkeloos" , "kort", "kortom" , "kortweg" , "koud" , "krankzinnig" 
                     , "kwalijk" , "laatst" , "langs" , "languit" , "langzamerhand" , "later" , "lekker" , "lekker"  
                     , "lichtelijk" , "liefst" , "liever" , "linksaf" , "losjes" , "louter" , "luidkeels" , "maar" 
                     , "machtig" , "maximaal" , "mede" , "medio" , "mee" , "meer" , "meestal" , "met" , "meteen" , "mettertijd" 
                     , "min" , "minder" ,  "minimaal" , "minstens" , "misschien" , "mogelijk" , "momenteel" , "morgen" , "na" , "naderhand" 
                     , "nadien", "nagenoeg" , "namelijk" , "nauwelijks" , "neer" , "nergens" , "net" , "niet" , "niets" 
                     , "niettemin" , "nihil" , "niks" , "nimmer" , "nochtans" , "nodeloos" , "nog" , "nogal" , "nogmaals" 
                     , "noodgedwongen" , "nooit" , "normaliter" , "nou" , "nu" , "ogenblikkelijk" , "ogenschijnlijk" , "oke" 
                     , "om" , "omheen" , "omhoog" , "omlaag" , "omver" , "omwille" , "onder" , "onderaan" , "onderdoor" 
                     , "onderhand" , "onderin" , "ondersteboven" , "ondertussen" , "onderuit" , "onderweg" , "onderwijl" 
                     , "ongemoeid" ,  "ongeveer" , "onlangs" , "onmiddellijk" , "onnodig" , "onomwonden" , "onophoudelijk" 
                     , "ontaard" , "ontiegelijk" , "ontzettend" , "onverwacht" , "onverwachts" , "onwel" , "ooit" , "ook" 
                     , "oorspronkelijk" , "op" , "opeen" , "opeens" , "oplettend" , "opnieuw" , "opzij" , "oudsher" , "over"  
                     , "overal" , "overboord" , "overdag" , "overeind" , "overheen" , "overhoop" , "overigens" , "overmorgen" 
                     , "overstag" , "overweg" , "overwegend" , "pal" , "pas" , "per se" , "permanent" , "perplex" , "playback" 
                     , "pletter" , "plots" , "plus" , "plusminus" , "praktisch" , "prima" , "pro" , "quasi" , "rakelings" 
                     , "rechtdoor" , "rechtop" , "rechtsaf" , "redelijk" , "reeds" , "regelrecht" , "respectievelijk" , "retour" 
                     , "reuze" , "rond" , "ronduit" , "ruggelings" , "ruimschoots" , "samen" , "schijnbaar" , "schoon" , "sindsdien" 
                     , "slecht" , "slechts" , "soms" , "speciaal"  
                     , "spoedig" , "spoorloos" , "steeds" , "steevast" , "stijf", "stinkend" , "straal" , "straks" , "stug" , "tamelijk" 
                     , "te" , "tegelijk" , "tegelijkertijd" , "tegemoet" , "tegen" , "tegenaan" , "telkens" , "temeer" , "tenminste" 
                     , "tenslotte" , "terdege" , "terecht" , "ternauwernood" , "terug" , "terwijl" , "tevens" , "tevoren" , "thans" 
                     , "thuis" , "tig" , "toch" , "toe" , "toen" , "toentertijd" , "trouwens" , "tussenbeide" , "tussendoor" , "tussentijds" 
                     , "uit" , "uiteen" , "uiteraard" , "uiterlijk" , "uitermate" , "uiterst" , "uitgerekend" , "uitgesproken" 
                     , "uitsluitend" , "up to date" , "vaak" , "van" , "vanavond" , "vandaag" , "vandaan" , "vandaar" , "vanmiddag" 
                     , "vanmorgen" , "vannacht" , "vanochtend" , "vanzelf" , "vast", "veel" , "veelal" , "veelvuldig" , "ver"
                     , "verder" , "verschrikkelijk" , "veruit" , "vervolgens" , "vierkant" , "vlak" , "volkomen" , "volledig" 
                     , "volop" , "voluit" , "voor" , "voor" , "vooraan" , "vooraf" , "vooral" , "vooralsnog" , "voorbij" 
                     , "voorgoed" , "voorheen" , "voornamelijk" , "voorover" , "voort" , "voortaan" 
                     , "voorts" , "vooruit" , "voorwaarts" , "voren" , "vreselijk" , "vrijuit" , "vrijwel" , "vroeger" , "waar" 
                     , "waarachtig" , "waarlijk" , "waarom" , "wanneer" , "wat" , "wederom" , "weer" , "weg" , "weinig" , "wel" , "weldra" 
                     , "weleens" , "weliswaar" , "wellicht" , "zachtjes" , "zeer", "zeker" , "zelden" , "zelfs" , "zienderogen" 
                     , "zijdelings" , "zo" , "zo-even" , "zoal" , "zodanig" , "zodoende" , "zojuist" , "zolang" , "zomaar" , "zoveel" , "zover" 
                     , "zowaar" , "zowat" , "zowel" , "zozeer" , "zuiver", "ik", "is", "het" , "dat", "op", "onwaarachtig", "hun", "bij", "weet"
                     ]
                    
    for woordInWoorden in lsWoorden:
            for wordInBijWrd in lsBijWoorden:
                if woordInWoorden.lower() != wordInBijWrd.lower():
                    strWord =  woordInWoorden.lower()
                    
                if woordInWoorden.lower() == wordInBijWrd.lower():
                    check = 1
                    
            if check == 0:        
                lsWords.append(strWord)
                
            if check == 1:
                check = 0
    
    return(lsWords)

def fltrIcons (lsWoorden):
    lsWords = [] 
    strWord = ""
    check = 0
    
    lsIcons = ["@","#","&","amp;","amp",";",":","http"]

    for woordInWoorden in lsWoorden:
        for wordInIncons in lsIcons:
            if woordInWoorden.lower() != wordInIncons:
                strWord =  woordInWoorden.lower()
                
            if woordInWoorden.lower() == wordInIncons:
                check = 1
                
        if check == 0:            
           lsWords.append(strWord)
        
        if check == 1:
            check = 0
        
    
    return(lsWords)

#lsfltrStopWoorden = fltrStopWoorden("@scheepvaartkrnt Ik weet dat reactie #Rabobank op #Zembla onwaarachtig is Het beeld op TV is hun praktijk bij #renteswaps &amp; #bijzonderbeheer")
#lsBijwoorden = fltrBijWoorden(lsfltrStopWoorden)
#lsIcons = fltrIcons(lsBijwoorden)

#print lsIcons

import json
tweets = []

for line in open('TwitterMessage.csv'):
  try: 
    tweets.append(json.loads(line))
  except:
    pass

#print len(tweets)
tweet = tweets[0]
#print tweet


texts = [tweet['text'] for tweet in tweets]
print texts[2]
     

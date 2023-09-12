import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "(#agnipath OR #Agnipath OR #agniveer OR #Agniveer OR #AgnipathScheme OR #agnipathscheme OR #Agnipathscheme OR #agnipathScheme) lang:en"
tweets = []
limit = 5000


for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    
    # print(vars(tweet))
    # break
    if len(tweets) == limit:

        break
    else:
        tweets.append([tweet.content])
        
df = pd.DataFrame(tweets, columns=['Tweet'])

df.to_csv('tweetUpdated.csv')
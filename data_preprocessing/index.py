import datapreprocessing as preprocessor
import TextRank4Keyword as textranker
import numpy as np
import importlib

preprocessor.preprocess()


# Generate frequency map of keywords in tweets
tweets=(preprocessor.getTrainSet())['tidy_tweet']
freq={}
for tweet in tweets:
    keywords=tweet
    for keyword in keywords:
        if(keyword in freq):
            freq[keyword]+=1
        else:
            freq[keyword]=1

freq = sorted(freq.items(), key=lambda item: item[1],reverse=True)

# Return top 50 keywords
print(freq[:50],sep="\n")



#Use TextRank model to get keywords
tweets=(preprocessor.getTrainSet())['basic_clean_tweet']
tr=textranker.TextRank4Keyword()
tweetString = ' '.join(tweets)
tr.analyze(tweetString, candidate_pos = ['NOUN', 'PROPN'], window_size=4, lower=False)
tr.get_keywords(50)
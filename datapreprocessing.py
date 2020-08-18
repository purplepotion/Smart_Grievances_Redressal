import re
import os,sys
import pandas as pd 
import numpy as np 
import string
import warnings
import datetime
from time import sleep  # Used for limiting API calls
import pickle
import textblob
from textblob import TextBlob
from collections import OrderedDict
import nltk
from nltk.stem.porter import * 
from nltk.stem import PorterStemmer


warnings.filterwarnings("ignore", category=DeprecationWarning)

# Add virtual env path to sys.path
current_working_directory = os.getcwd()
if current_working_directory not in sys.path:
    sys.path.append(current_working_directory)

#%matplotlib inline

#Preprocessing for sentiment analysis
def clean_tweet(tweet): 
    ''' 
    Utility function to clean tweet text by removing links, special characters 
    using simple regex statements. 
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split()) 
  
def get_tweet_sentiment(tweet): 
    ''' 
    Utility function to classify sentiment of passed tweet 
    using textblob's sentiment method 
    '''
    # create TextBlob object of passed tweet text 
    analysis = TextBlob(clean_tweet(tweet)) 
    # set sentiment 
    if analysis.sentiment.polarity < 0: 
        return 1
    else: 
        return 0


# loading training and test data

train  = pd.read_csv('Dataset/finalDate.csv',encoding="ISO-8859-1")
# Drop unnamed columns
train.drop(train.columns[train.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
train.replace('', np.nan, inplace=True)
train.dropna(inplace=True)
# Remove non-utf characters
train['tweet']=train['tweet'].apply(lambda x: ''.join(["" if  i not in  string.printable else i for i in x]))

#combining training and and test data for preprocessing 
total_data = train

#Generate modules for the task
def preprocess():
    removePattern()
    removeShortWords()
    # tokenized_tweet = tokenize()
    # tokenized_tweet = stemWords(tokenized_tweet)
    # joinTokens(tokenized_tweet)
    # total_data['tidy_tweet'] = tokenized_tweet
    print("\n\nPreprocessing done\n\n")
    

def getTrainSet() :
    return train

# def getTestSet() :
#     return test

def getTotalSet() :
    return total_data


#function to remove @word pattern from the tweets as they do not add any value

def removePatternUtil(input_txt, pattern):
    r = re.findall(pattern, input_txt)
    for i in r:
        input_txt = re.sub(i, '', input_txt)
        
    return input_txt

# removing @username patterns from tweets using remove_pattern function
def removePattern():
    print('\n\nRemoving  Twitter Handles \n\n')
    total_data['tidy_tweet'] = np.vectorize(removePatternUtil)(total_data['tweet'], "@[\w]*")
    total_data.head()

# words with small lenght i.e., words having length smaller than 3 hardly hold any sentiment
# hence it is better to remove such words
def removeShortWords():
    print('\n\nRemoving Short Words\n\n')
    total_data['tidy_tweet'] = total_data['tidy_tweet'].apply(lambda x: ' '.join([w for w in x.split() if len(w)>3]))
    total_data.head()

# separating each word as a token
def tokenize():
    print('\n\nTweet Tokenization\n\n')
    tokenized_tweet = total_data['tidy_tweet'].apply(lambda x: x.split())
    return tokenized_tweet


# removing punctuations like period, comma and semi-colon seems like a good idea but it is actually decreasing the accuracy 
def removePunctuation(tokenized_tweet):
    tokenized_tweet=tokenized_tweet.apply(str)
    '''
    #removing punctuations from each word if any
    len(tokenized_tweet)
    for i in range(len(tokenized_tweet)):
        for j in range(len(tokenized_tweet[i])):
            tokenized_tweet[i][j]=tokenized_tweet[i][j].replace('[.,;:]','')
    '''
    return tokenized_tweet;    
       
# stemming words i.e, words are play,playing,played are treated similarly
def stemWords(tokenized_tweet):
    print('\n\nStemming\n\n')
    stemmer = PorterStemmer()
    tokenized_tweet = tokenized_tweet.apply(lambda x: [stemmer.stem(i) for i in x])
    return tokenized_tweet

#stiching these tokens together
def joinTokens(tokenized_tweet):
    # remove non ascii characters
    tokenized_tweet =  [re.sub(r'[^\x00-\x7F]+','', str(x)) for x in tokenized_tweet]
    for i in range(len(tokenized_tweet)):
        tokenized_tweet[i] = ' '.join(tokenized_tweet[i])
    

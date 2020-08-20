import re
import string
import warnings
import datetime
import nltk
from nltk.stem.porter import * 
from nltk.stem import PorterStemmer
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english')) 

def preprocess(string):
    res = removePatternUtil(string, "@[\w]*")
    res = keepAlphaNumericChars(string)
    res = removeShortWords(res)
    res = removeStopWords(res)
    tokens = stemWords(res)
    return tokens

def removePatternUtil(input_txt, pattern):
    r = re.findall(pattern, input_txt)
    for i in r:
        input_txt = re.sub(i, '', input_txt)
    return input_txt

def keepAlphaNumericChars(string):
    re.sub(r'\W+', '',string)
    return string

def removeShortWords(string):
    string= ' '.join([w for w in string.split() if len(w)>3])
    return string

def removeStopWords(string):
    string= ' '.join([w for w in string.split() if w not in stop_words])
    return string

def stemWords(string):
    porter = PorterStemmer()
    tokenized_tweet =string.split()
    tokenized_tweet=[porter.stem(word) for word in tokenized_tweet]
#     tokenized_tweet =  ' '.join(w for w in tokenized_tweet)
    return tokenized_tweet

def generateKeywordDictionary(tweets,departments):
    table={}
    for tweet,category in zip(tweets,departments):
        keywords = preprocess(str(tweet))
        if category not in table:
            table[category]=[]
            table[category].extend(keywords)
        else:
            for keyword in keywords:
                if keyword not in table[category]:
                    table[category].append(keyword)
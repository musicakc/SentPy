from __future__ import division
from string import punctuation
import urllib,os

pos_count = 0
neg_count = 0
url='http://www.unc.edu/~ncaren/haphazard/'
path = r'/home/amitoj/Projects/Sentiment Analysis/'

files=['negative.txt','positive_text','obama_tweets.txt']
for file_name in files:
    urllib.urlretrieve(url,file_name)

positive_words = ['awesome', 'good', 'nice', 'super','fun','delightful']
negative_words = ['awful', 'lame', 'horrible', 'bad']
emotional_words = negative_words + positive_words
tweet = 'Hello there! A beautiful day for a nice game!'
for p in list(punctuation):
    tweet = tweet.replace(p,'')
#tweetl = tweet.lower()
words = tweet.split(' ')
for word in words:
    if word.lower() in positive_words:
        print word.lower()
        pos_count += 1
for word in words:
    if word.lower() in negative_words:
        print word.lower()
        neg_count += 1

print pos_count/len(words)
print neg_count/len(words)

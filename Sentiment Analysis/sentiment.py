from __future__ import division
from string import punctuation
import urllib,os

pos_count = 0
neg_count = 0
url1='http://www.unc.edu/~ncaren/haphazard/negative.txt'
file_name1= 'negative.txt'
urllib.urlretrieve(url1,file_name1)

url2 ='http://www.unc.edu/~ncaren/haphazard/positive.txt'
file_name2 = 'positive.txt'
urllib.urlretrieve(url2,file_name2)

url3='http://www.unc.edu/~ncaren/haphazard/obama_tweets.txt'
file_name3= 'obama_tweets.txt'
urllib.urlretrieve(url3,file_name3)

#positive_words = ['awesome', 'good', 'nice', 'super','fun','delightful']
#negative_words = ['awful', 'lame', 'horrible', 'bad']
#emotional_words = negative_words + positive_words
tweets = open("obama_tweets.txt").read()
'''for p in list(punctuation):
    tweet = tweet.replace(p,'')
#tweetl = tweet.lower()'''
tweets_list = tweets.split('\n')

for tweet in tweets_list[0:10]:
    print tweet

print tweets_list[1:3]
#print pos_count/len(words)
#print neg_count/len(words)

from __future__ import division
from string import punctuation
import urllib
import csv

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


pos_sent = open("positive.txt").read()
positive_words = pos_sent.split("\n")
positive_count = []

neg_sent = open("positive.txt").read()
negative_words = pos_sent.split("\n")
negative_count = []

for tweet in tweets_list:
    positive_counter = 0
    negative_counter = 0

    tweet_processed = tweet.lower()

    for p in list(punctuation):
        tweet_processed = tweet_processed.replace(p,'')

    words = tweet_processed.split(' ')
    word_count = len(words)

    for word in words:
        if word in positive_words:
            positive_counter += 1
        elif word in negative_words:
            negative_counter += 1

    positive_count.append(positive_counter/word_count)
    negative_count.append(negative_counter/word_count)

print len(positive_count)

output = zip(tweets_list,positive_count,negative_count)

writer = csv.writer(open('tweet_sentiment.csv','wb'))
writer.writerows(output)

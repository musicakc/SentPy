from twython import Twython
import csv

TWITTER_APP_KEY = 'xTEdIvzBj3LTrwLRUuf84SyxM'
TWITTER_APP_KEY_SECRET = 'IX9NUd48EBccw0d3D1A0QiUaS79DlXhkVfZyOy5ZdBfPtOV3dW'
TWITTER_ACCESS_TOKEN = '566861858-HhaAzNvqvNont9Ft9nIBgHkjBl06kG3aupwQBBHC'
TWITTER_ACCESS_TOKEN_SECRET= 'YuAjsEkTGGTMdZoGyJVF7WmdxUHK4eUf4NNhKOFIMK3cr'

t = Twython(app_key=TWITTER_APP_KEY,
            app_secret=TWITTER_APP_KEY_SECRET,
            oauth_token=TWITTER_ACCESS_TOKEN,
            oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

search = t.search(q='#nepalearthquake',count=100)

tweets = search['statuses']
with open('tweets.csv','w') as f:
    for tweet in tweets:
        #f.write('Author,Date,Text')
        writer = csv.writer(f)
        data = [tweet['user']['screen_name'].encode('utf-8'),
                tweet['created_at'],
                tweet['text'].encode('utf-8')]
        writer.writerow(data)
        

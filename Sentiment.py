# To check whether Data can be fetched or not through Twitter API


import re
import tweepy
from tweepy import OAuthHandler
import csv

consumer_key = 'xxxxxxxxxxxxxxxxxxxxxxx'
consumer_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' #Authentication credential from twitter API
access_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

search = api.search("")

for items in search:
    print(items.text)

with open('example.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        print(row)

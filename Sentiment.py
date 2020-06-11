# To check whether Data can be fetched or not


import re
import tweepy
from tweepy import OAuthHandler
import csv

consumer_key = 'kUOXj04AsZSehVlEbfcBu5Sdd'
consumer_secret = 'N8P5RENGsEBSsMnjZACcUjd8PHHvehq1UmMslnoj2N3t9Eg8KK'
access_token = '1108590279400001537-45wvua5g6QQPWQP8caf10RwUiAcDW7'
access_secret = 'q6dVXr3DRu5OoT1YOiT1iQOnHow2OJ4T6n2lGrYoEtWR7'

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

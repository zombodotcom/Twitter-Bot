import tweepy, sys, time
from random import randint
from keys import keys
 
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']
 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
 
handles = sys.argv[1]
f = open(handles, "r")
h = f.readlines()
m1= open(sys.argv[2],'r').read()  #message.txt or whatever you want to call the message file
f.close()
 
for i in h: #loop through handle list
    i = i.rstrip()
    m = i + " " + m1 
    s = api.update_status(m)
    nap = randint(1, 60)#random wait time change this 1-60 seconds 
    time.sleep(nap)
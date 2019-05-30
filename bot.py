import time

import tweepy
CONSUMER_KEY="4KcF41g7EdoPXvRydbtQzhhSk"
CONSUMER_SECRET="buS7tTKWJDawTB6O5OIhzCG8hEdmZC9dBqRM5Iu4HwVC4ImggU"
ACCESS_KEY="1133793550838185985-JjgE3stD6tM1tDjnXkjo6FPgejPa9N"
ACCESS_SECRET="BBvCb7XSsBPRMrL2nFXaFpt7tOQRUrv8Vd21PqBHKzTSd"
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api=tweepy.API(auth)
mentions = api.mentions_timeline()
user=api.me()
print(user.name)
#lc=time.localtime(time.time())
#if lc.tm_min%5==0:
    #api.update_status(time.asctime(time.localtime(time.time())))
s="टन "
lc=time.localtime(time.time())
def tweet_time():
    lc=time.localtime(time.time())
    if lc.tm_min==0 and lc.tm_sec==0:
        if lc.tm_hour<12:
            api.update_status(s*lc.tm_hour +"\n" + str(lc.tm_hour) +'AM IST')
        else:
            x=lc.tm_hour
            x=x-12
            api.update_status(s*x +"\n" + str(x) +'PM IST')




while(1>0):        
    tweet_time()

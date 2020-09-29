import time
from time import sleep
import tweepy
CONSUMER_KEY=""
CONSUMER_SECRET=""
ACCESS_KEY=""
ACCESS_SECRET=""
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
    x=lc.tm_min
    y=lc.tm_sec
    if lc.tm_min==0 and y==0:
        if lc.tm_hour<12:
            api.update_status(s*lc.tm_hour +"\n" + str(lc.tm_hour) +'AM IST')
            y=y+1
        else:
            x=lc.tm_hour
            x=x-12
            api.update_status(s*x +"\n" + str(x) +'PM IST')
            y=y+1

def like_hashtags():
    for tweet in tweepy.Cursor(api.search, q=('#WomenWhoCode OR #100DaysOfCode OR #WomenInTech -filter:retweets')).items(5):
        try:
            print('\nLike Bot found tweet by @' + tweet.user.screen_name + '. ' + 'Attempting to like.')

            tweet.favorite()
            tweet.retweet()
            print('LIKE published successfully.')

            # Where sleep(10), sleep is measured in seconds.
            # Change 10 to amount of seconds you want to have in-between retweets.
            # Read Twitter's rules on automation. Don't spam!
            sleep(60)

        # Some basic error handling. Will print out why retweet failed, into your terminal.
        except tweepy.TweepError as error:
            print('\nError. Like not successful. Reason: ')
            print(error.reason)
            break

        except StopIteration:
            break


while(1>0):
    tweet_time()
    like_hashtags()

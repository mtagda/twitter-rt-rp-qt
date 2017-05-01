from tweepy import OAuthHandler, API
from TwitterSearch import *

consumer_key = 'aaaa'
consumer_secret = 'bbbb'
access_token = 'cccc'
access_token_secret = 'dddd'

auth = OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)
auth.set_access_token(key=access_token, secret=access_token_secret)
api = API(auth)

class GetStatusRetweets(object):
    def __call__(self, status_id, screen_name):
        # Check input data
        if type(status_id) is not int:
            print("""'status_id' should be an integer""")
            return

        if type(screen_name) is not str:
            print("""'screen_name' should be a string""")
            return

        # Create a TwitterSearchOrder object
        tso = TwitterSearchOrder()
        keywords = '@' +str(screen_name) + ' include:retweets'
        tso.set_keywords([keywords])

        # Create a TwitterSearch object with secret tokens
        ts = TwitterSearch(
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token=access_token,
            access_token_secret=access_token_secret)

        # Searching for Quote Tweets of the Status
        try:
            for tweet in ts.search_tweets_iterable(tso):
                if 'quoted_status' in tweet:
                    if tweet['quoted_status']['id'] == status_id:
                        yield tweet

        except TwitterSearchException as e:
            print(e)

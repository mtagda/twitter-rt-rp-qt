# twitter-rt-rp-qt
Find all retweets/replies/quote tweets of some Twitter status which were published the last 7 days

EXAMPLE: 

We want to find all retweets/replies/quote tweets of Twitter status 123456789.

    getU = GetUserFromStatus()
    getRTRPQT = GetStatusRTAndRP()
    status_id = 123456789
    user_screen_name = getU.call(status_id)
    file = open('tweets2.txt', 'w')
    
    for tweet in getRTRPQT(status_id, user_screen_name):
        file.write(tweet['user']['screen_name'])
    

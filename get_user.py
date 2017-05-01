from tweepy import OAuthHandler, API

consumer_key = 'aaaa'
consumer_secret = 'bbbb'
access_token = 'cccc'
access_token_secret = 'dddd'

auth = OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)
auth.set_access_token(key=access_token, secret=access_token_secret)
api = API(auth)


class GetUserFromStatus(object):
    def call(self, status_id):
        # Check input data
        if type(status_id) is not int:
            print("""'status_id' should be an integer""")
            return

        user_id = self.get_user_id(status_id)
        screen_name = self.get_screen_name(user_id)
        return screen_name

    @staticmethod
    def get_user_id(status_id):
        # Find id of user who posted given status
        try:
            query = api.statuses_lookup(id_=[status_id], include_entities=True, trim_user=True)
            for status in query:
                return status.user.id
        except:
            print('Given status is more than 7 days old')

    @staticmethod
    def get_screen_name(user_id):
        # Find screen name for given user_id
        return api.get_user(user_id).screen_name

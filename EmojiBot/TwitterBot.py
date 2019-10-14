import tweepy


class EmojiListener(tweepy.StreamListener):
    def __init__(self, api, emojifier):
        self.api = api
        self.emojifier = emojifier

    def on_status(self, status):
        print('I still do not know how to answer with images :(')


def twitter_bot(token, emoji_directory, scale, pattern):
    # Authenticate to Twitter
    consumer_key, consumer_secret, access_token, access_token_secret = \
        token.split(':')

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    # Load emojifier
    from Emojifier import Emojifier
    emojifier = Emojifier.create_from_directory(emoji_directory)

    listener = EmojiListener(api, emojifier)

    stream = tweepy.Stream(auth=api.auth, listener=listener)
    stream.filter(track=['EmojiArtsBot'])

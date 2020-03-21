import io
import tweepy
import requests
import traceback
import imageio


BOT_NAME = 'EmojiArtsBot'


class EmojiListener(tweepy.StreamListener):
    def __init__(self, api, emojifier, scale, pattern):
        super().__init__(api)
        self.emojifier = emojifier
        self.scale = scale
        self.pattern = pattern


    def on_status(self, status):
        tweet_author = status.author.screen_name
        if tweet_author == BOT_NAME and 'First' not in status.text:
            return
        try:
            answer =\
                    [
                        self.emojifier.emojify_image(
                            imageio.imread(
                                io.BytesIO(
                                    requests.get(
                                        media.get('media_url')
                                    ).content
                                )
                            ),
                            self.scale,
                            self.pattern
                        )
                        for media in status.entities.get('media', [])
                    ]
            if answer:
                for (i, photo) in enumerate(answer):
                    photo_stream = io.BytesIO()
                    imageio.imsave(photo_stream, photo, format='png')
                    photo_stream.seek(0)
                    self.api.update_with_media(
                        f'image_{i}.png',
                        file=photo_stream,
                        in_reply_to_status_id=status.id
                    )

        except Exception as e:
            traceback.print_exc()


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

    listener = EmojiListener(api, emojifier, scale, pattern)

    stream = tweepy.Stream(auth=api.auth, listener=listener)
    stream.filter(track=[BOT_NAME])

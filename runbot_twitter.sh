#!/bin/bash
set -x
python EmojiBot/EmojiBot.py --twitter_token=${EMOJI_TWITTER_API_KEY}:${EMOJI_TWITTER_PRIVATE_API_KEY}:${EMOJI_TWITTER_ACCESS_KEY}:${EMOJI_TWITTER_ACCESS_SECRET} resources/emojis72 --scale=0.4

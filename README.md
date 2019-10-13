# emoji-bot

A telegram bot which makes emoji-art from a given image (see the example below). The original idea and implementation is from @JfonS. This repo was originally a fork from JfonS/emogi-bot.

This implementation works in O(n^2 + (n^2 / d^2) log m ) when applying the grid pattern by searching the closest emoji in a KD-Tree instead of a list.

## Supported platforms
- Telegram

## WiP
- Twitter

## Dependencies
See requirements.txt

## How to run it
```
usage: EmojiBot.py [-h] [--telegram_token TELEGRAM_TOKEN]
                   [--twitter_token TWITTER_TOKEN] [-s SCALE] [-p PATTERN]
                   emoji_directory

A Multi-Platform Bot to convert images to emoji art

positional arguments:
  emoji_directory       Path to directory with emoji images

optional arguments:
  -h, --help            show this help message and exit
  --telegram_token TELEGRAM_TOKEN
                        Telegram Bot API Token (see BotFather if you do not
                        know what is this)
  --twitter_token TWITTER_TOKEN
                        OAuth token for Twitter
  -s SCALE, --scale SCALE
                        Emoji scale factor
  -p PATTERN, --pattern PATTERN
                        Emoji filling pattern
```

## Example
![Kylo Ren](https://github.com/srgrr/emoji-bot/blob/master/resources/kylo.jpeg "meow!")

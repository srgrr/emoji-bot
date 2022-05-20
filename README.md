# Emoji-bot

A multi-platform bot to make emoji-art from a given image (see the example below).

This project started as an excuse to find a "practical" application of KD-Trees, a data structure I like a lot.

## Supported platforms
- Telegram

## Dependencies
See requirements.txt

## How to run it
```
usage: EmojiBot.py [-h] [--telegram_token TELEGRAM_TOKEN]
                   [--benchmark_image BENCHMARK_IMAGE] [-s SCALE] [-p PATTERN]
                   emoji_directory

A Multi-Platform Bot to convert images to emoji art

positional arguments:
  emoji_directory       Path to directory with emoji images

optional arguments:
  -h, --help            show this help message and exit
  --telegram_token TELEGRAM_TOKEN
                        Telegram Bot API Token (see BotFather if you do not
                        know what is this)
  --benchmark_image BENCHMARK_IMAGE
                        Process a single image for testing purposes
  -s SCALE, --scale SCALE
                        Emoji scale factor
  -p PATTERN, --pattern PATTERN
                        Emoji filling pattern
```

## Example
![Kylo Ren](https://github.com/srgrr/emoji-bot/blob/master/resources/kylo.jpeg "meow!")

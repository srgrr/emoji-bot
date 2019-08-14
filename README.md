# emoji-bot

A telegram bot which makes emoji-art from a given image (see the example below, meow!). The original idea and implementation is from @JfonS. This repo was originally a fork from JfonS/emogi-bot.

This implementation works in O(n^2 + (n^2 / d^2) log m ) when applying the grid pattern by searching the closest emoji in a KD-Tree instead of a list.

## Dependencies
- python 3.x (python 2.x is not guaranteed to work, python2.6 does not work for
  sure due to argparse)
- pyTelegramBotApi
- pillow
- numpy
- scipy

## How to run it
- Get a token from the botFather bot at Telegram
- Configure your bot (i.e: add commands if you want, etc)
- Run the following command: python(3) main.py YOUR_TOKEN emoji_directory --pattern [grid | random]
- Send a photo. Then wait a second or two... and profit!!!


## Meow
![meow](https://github.com/srgrr/emoji-bot/blob/master/resources/jero2.jpeg "meow!")

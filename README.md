# emoji-bot

A telegram bot that makes emoji-art from a given image (see the example below, meow!). The original idea and implementation is from @JfonS. This repo was originally a fork from JfonS/emogi-bot.

This algorithm computes the mean color for each subgrid that has the same size as the image of the emojis and searches the emoji with the closest mean color. This can be implemented in a naive way in O(n^2 + (n^2 / d^2) * m), where n is the length of the largest side of the image, d is the length of the largest side of the emojis, and m is the total number of emojis.

This implementation works in O(n^2 + (n^2 / d^2) log m ) by searching the closest emoji in a KD-Tree instead of in a list.

## Dependencies
- python 3.x (python 2.x is not guaranteed to work)
- pyTelegramBotApi
- pillow
- numpy
- scipy

## How to run it
- Get a token from the botFather bot at Telegram
- Configure your bot (i.e: add commands if you want, etc)
- Run the following command: python(3) main.py YOUR_TOKEN --emoji_resolution R
  --force_precompute (if wanted)
- Send a photo. Then wait a second or two... and profit!!!


## Meow
![meow](https://github.com/srgrr/emoji-bot/blob/master/resources/jero.jpg "meow!")

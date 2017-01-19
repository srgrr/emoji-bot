import os
import sys
import numpy as np
import random
import telebot
import requests
import subprocess
try:
	import cStringIO as StringIO
except:
	import StringIO

from precompute import get_precomputed_dict
from scipy import misc
from scipy.spatial import KDTree
from img2emoji import img2emoji

# read configuration parameters
config = eval(open("config.cfg").read())

# load the emojis and store them in a dict of the form {mean : image}
image_dict = get_precomputed_dict(config["EMOJI_SOURCE"], config["FORCE_RECALC"])
image_points = np.array([list(p) for p in image_dict.keys()])
search_tree = KDTree(image_points)
emoji_height, emoji_width, _ = image_dict[tuple(image_points[0])].shape

# initialize the bot
TOKEN = sys.argv[1]
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['help', 'start'])
def help(msg):
	"""
		Help command.
	"""
	bot.send_message(msg.chat.id, "I convert images to emoji art. Send a picture to me. Eloy Emilio Concepto")

@bot.message_handler(content_types=['photo'])
def handle_images(message):
	"""
		Given a photo, tries to create an emoji-art image from it.
		If it is not possible, then a simple message will be displayed instead.
	"""
	try:
		# read the image and put it in a np.ndarray
		photo = message.photo[-1]
		image_file_path = bot.get_file(photo.file_id).file_path
		local_file_path = os.path.join(os.path.split(sys.argv[0])[0], str(random.randint(0, 2**64 - 1))+".png")
		image_file = bot.download_file(image_file_path)
		f = StringIO.StringIO(image_file)
		image_content = misc.imread(f)
		# get the emoji-art image
		ret = img2emoji(image_content, image_dict, search_tree)
		# save the image in png format, then send it
		misc.imsave(local_file_path, ret)
		send_image = open(local_file_path, 'rb')
		bot.send_photo(message.chat.id, send_image)
		subprocess.Popen(['python', 'file_deleter.py', local_file_path])
	except:
		# :(
		bot.reply_to(message, "Something went wrong. Sorry :(")

bot.polling()

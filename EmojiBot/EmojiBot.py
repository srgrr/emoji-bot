def main(TOKEN, emoji_directory):
	import telebot
	bot = telebot.TeleBot(TOKEN)
	from Emojifier import Emojifier
	emojifier = Emojifier.create_from_directory(emoji_directory)

	@bot.message_handler(commands = ["help", "start"])
	def help(message):
		bot.send_message(
			message.chat.id,
			"Hello! I convert images to emoji art, send me a picture and see what happens!"
			)

	@bot.message_handler(content_types = ["photo"])
	def handle_picture(message):
		picture = message.photo
		print(picture)


	bot.polling()

if __name__ == '__main__':
	import CommandLine as CL
	options = CL.parse_arguments()
	main(**vars(options))

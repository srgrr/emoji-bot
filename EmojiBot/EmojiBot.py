def main(TOKEN, emoji_directory, scale_factor, pattern):
	import telebot
	bot = telebot.TeleBot(TOKEN)
	from Emojifier import Emojifier
	emojifier = Emojifier.create_from_directory(emoji_directory, scale_factor)

	@bot.message_handler(commands = ["help", "start"])
	def help(message):
		bot.send_message(
			message.chat.id,
			"Hello! I convert images to emoji art, send me a picture and see what happens!"
			)

	@bot.message_handler(content_types = ["photo"])
	def handle_picture(message):
		photo = message.photo[-1]
		image_file_path = bot.get_file(photo.file_id).file_path
		image_content = bot.download_file(image_file_path)
		from scipy import misc
		from io import BytesIO
		picture = misc.imread(BytesIO(image_content))

		result = emojifier.emojify_image(picture, pattern)

		output = BytesIO()

		misc.imsave(output, result, format = "png")

		output.seek(0)

		bot.send_photo(message.chat.id, output)

	bot.polling()

if __name__ == '__main__':
	import CommandLine as CL
	options = CL.parse_arguments()
	main(**vars(options))

import telebot
import traceback
from Emojifier import Emojifier
from scipy import misc
from io import BytesIO


def telegram_bot(token, emoji_directory, scale, pattern):
    bot = telebot.TeleBot(token)
    emojifier = Emojifier.create_from_directory(emoji_directory)

    @bot.message_handler(commands=['help', 'start'])
    def help(message):
        bot.send_message(
            message.chat.id,
            (
                'Hello! I convert images to emoji art, send'
                ' me a picture and see what happens!\n'
                'Source code: https://github.com/srgrr/emoji-bot'
            )
        )

    @bot.message_handler(content_types=['photo'])
    def handle_picture(message):
        try:
            photo = message.photo[-1]
            image_file_path = bot.get_file(photo.file_id).file_path
            image_content = bot.download_file(image_file_path)
            picture = misc.imread(BytesIO(image_content))
            result = emojifier.emojify_image(picture, scale, pattern)
            output = BytesIO()
            misc.imsave(output, result, format='png')
            output.seek(0)
            bot.send_photo(message.chat.id, output)
        except Exception as e:
            traceback.print_exc()
            bot.send_message(
                message.chat.id,
                'Something went wrong. Sorry :('
            )

    bot.polling()

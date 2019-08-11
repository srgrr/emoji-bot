class DEFAULTS:
	pass

def _get_parser():
	from argparse import ArgumentParser

	parser = ArgumentParser(
		description = "A Telegram Bot which converts images to emoji art"
		)

	parser.add_argument(
		"TOKEN",
		type = str,
		help = "Telegram Bot API Token (see BotFather if you do not know what is this)"
		)

	parser.add_argument(
		"emoji_directory",
		type = str,
		help = "Path to directory with emoji images"
		)

	return parser

def _check_arguments(options):
	from argparse import ArgumentTypeError
	pass

def parse_arguments():
  ret =  _get_parser().parse_args()
  _check_arguments(ret)
  return ret
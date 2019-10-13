def main():
    import CommandLine as CL
    options = CL.parse_arguments()
    bot_options = {
        'emoji_directory': options.emoji_directory,
        'scale': options.scale,
        'pattern': options.pattern
    }
    if options.telegram_token:
        from TelegramBot import telegram_bot as bot_main
        bot_options['token'] = options.telegram_token
    elif options.twitter_token:
        from TwitterBot import twitter_bot as bot_main
        bot_options['token'] = options.twitter_token
    bot_main(**bot_options)


if __name__ == '__main__':
    main()
else:
    raise ImportError((
            'This is not a Python package '
            'and it should never be imported'
        )
    )

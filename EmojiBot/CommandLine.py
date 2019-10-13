class DEFAULTS:
    SCALE_FACTOR = 0.8
    PATTERN = 'timelimit'


def _get_parser():
    from argparse import ArgumentParser

    parser = ArgumentParser(
        description='A Multi-Platform Bot to convert images to emoji art'
        )

    parser.add_argument(
        '--telegram_token',
        type=str,
        help=(
            'Telegram Bot API Token (see BotFather '
            'if you do not know what is this)'
        )
    )

    parser.add_argument(
        '--twitter_token',
        type=str,
        help='OAuth token for Twitter'
    )

    parser.add_argument(
        'emoji_directory',
        type=str,
        help='Path to directory with emoji images'
        )

    parser.add_argument(
        '-s',
        '--scale',
        type=float,
        default=DEFAULTS.SCALE_FACTOR,
        help='Emoji scale factor'
        )

    parser.add_argument(
        '-p',
        '--pattern',
        type=str,
        default=DEFAULTS.PATTERN,
        help='Emoji filling pattern'
        )

    return parser


def _check_arguments(options):
    from argparse import ArgumentTypeError
    if not (options.telegram_token or options.twitter_token):
        raise ArgumentTypeError('At least one platform token is necessary')
    if options.telegram_token and options.twitter_token:
        raise ArgumentTypeError('Multiple tokens provided')


def parse_arguments():
    ret = _get_parser().parse_args()
    _check_arguments(ret)
    return ret

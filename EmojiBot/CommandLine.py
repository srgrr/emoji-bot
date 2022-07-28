from argparse import ArgumentParser, ArgumentTypeError


class DEFAULTS:
    SCALE_FACTOR = 1.0
    PATTERN = 'grid'


def _get_parser():
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
        '--benchmark_image',
        type=str,
        help=(
            'Process a single image '
            ' for testing purposes')
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
    tokens =\
        [
            options.telegram_token,
            options.benchmark_image
        ]
    if sum(int(x is not None) for x in tokens) != 1:
        raise ArgumentTypeError(
            'Exactly one platform token or image benchmark is necessary'
        )


def parse_arguments():
    ret = _get_parser().parse_args()
    _check_arguments(ret)
    return ret

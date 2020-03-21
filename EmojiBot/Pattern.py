class Pattern(object):

    def __init__(self, height, width, emoji_height, emoji_width):
        self.height = height
        self.width = width
        self.emoji_height = emoji_height
        self.emoji_width = emoji_width


class GridPattern(Pattern):

    def __init__(self, height, width, emoji_height, emoji_width):
        Pattern.__init__(self, height, width, emoji_height, emoji_width)

    def get_pattern_sequence(self):
        for i in range(0, self.height, self.emoji_height):
            for j in range(0, self.width, self.emoji_width):
                yield \
                    [
                        i,
                        j,
                        i + self.emoji_height - 1,
                        j + self.emoji_width - 1
                    ]


class PatternClassFactory(object):

    @staticmethod
    def get_from_string(key):
        if key == 'grid':
            return GridPattern
        raise Exception(f'Invalid pattern name (received {key})')

class Pattern(object):
	
	def __init__(self, height, width, emoji_height, emoji_width):
		self.height = height
		self.width  = width
		self.emoji_height = emoji_height
		self.emoji_width = emoji_width

class GridPattern(Pattern):
	
	def __init__(self, height, width, emoji_height, emoji_width):
		Pattern.__init__(self, height, width, emoji_height, emoji_width)

	def get_pattern_sequence():
		
		for i in range(0, height, emoji_height):
			for j in range(0, width, emoji_width):
				yield [i, j, i + emoji_height - 1, j + emoji_width - 1]

class RandomPattern(Pattern):

	def __init__(self, height, width, emoji_height, emoji_width):
		Pattern.__init__(self, height, width, emoji_height, emoji_width)	

	def get_pattern_sequence():
		pass


class PatternFactory(object):
	@staticmethod
	def get_from_string(self, key):
		if key == "grid":
			return GridPattern
		elif key == "random":
			return RandomPattern

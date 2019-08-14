class Pattern(object):
	
	def __init__(self, height, width, emoji_height, emoji_width):
		self.height = height
		self.width  = width
		self.emoji_height = emoji_height
		self.emoji_width = emoji_width

class GridPattern(Pattern):
	
	def __init__(self, height, width, emoji_height, emoji_width):
		Pattern.__init__(self, height, width, emoji_height, emoji_width)

	def get_pattern_sequence(self):
		for i in range(0, self.height, self.emoji_height):
			for j in range(0, self.width, self.emoji_width):
				yield [i, j, i + self.emoji_height - 1, j + self.emoji_width - 1]

class RandomPattern(Pattern):

	def __init__(self, height, width, emoji_height, emoji_width):
		Pattern.__init__(self, height, width, emoji_height, emoji_width)	

	def get_pattern_sequence(self):
		from math import sqrt
		num_patterns = int((4.5 * self.height * self.width) / sqrt(self.height * self.emoji_height))

		for _ in range(num_patterns):
			from random import randint
			t = randint(0, self.height - self.emoji_height - 1)
			l = randint(0, self.width  - self.emoji_width  - 1)
			yield [t, l, t + self.emoji_height - 1, l + self.emoji_width - 1]

class PatternClassFactory(object):

	@staticmethod
	def get_from_string(key):
		if key == "grid":
			return GridPattern
		elif key == "random":
			return RandomPattern
		raise Exception("Invalid pattern name (received %s)" % key)
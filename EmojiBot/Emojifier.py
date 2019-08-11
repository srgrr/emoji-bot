class Emojifier(object):

	def __init__(self, image_list):

		import numpy as np

		self.images = [
			img[:, :, :3]
			for img in image_list
		]
		
		means = [
			[int(np.mean(img[:, :, k])) for k in range(3)]
			for img in self.images
		]

		from scipy.spatial import KDTree	
		self.__tree = KDTree(means)

	@staticmethod
	def create_from_directory(directory):
		import glob
		import os
		from scipy import misc
		
		image_list = []
		
		for image in glob.glob(os.path.join(directory, "*")):
			image_list.append(
				misc.imread(image)
			)
		
		return Emojifier(image_list)

	def emojify_image(self, image, pattern_key):
		from Pattern import PatternFactory
		#pattern = PatternClassFactory.get_from_string(pattern_key)()
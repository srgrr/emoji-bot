import numpy as np
import datetime as dt

def img2emoji(image_content, image_dict, search_tree = None):
	"""
		Given a numpy.ndarray that represents an RGB image (with values in 0-255),
		a dictionary of the form {(R, G, B) : image} and, optionally, an scipy KD-Tree
		of the dictionary keys, creates an emoji-art image.
		If the KD-Tree is not specified it will be created
	"""
	image_points = np.array([list(p) for p in image_dict.keys()])
	emoji_height, emoji_width, _ = image_dict[tuple(image_points[0])].shape
	if search_tree is None:
		from scipy.spatial import KDTree
		search_tree = KDTree(image_points)
	image_sums = np.zeros(image_content.shape)

	start_time = dt.datetime.now()

	for k in range(3):
		image_sums[:, :, k] = np.cumsum(np.cumsum(image_content[:, :, k], axis = 0), axis = 1)
	image_height, image_width, _ = image_content.shape

	end_time = dt.datetime.now()

	print("Means comp: %f"%((end_time-start_time).microseconds/1e6))

	def sub_mean(i, j):
		ret = np.zeros(3)
		ret[:] = image_sums[i, j]
		if i >= emoji_height: ret -= image_sums[i - emoji_height, j]
		if j >= emoji_width : ret -= image_sums[i, j - emoji_width]
		if i >= emoji_height and j >= emoji_width: ret += image_sums[i - emoji_height, j - emoji_width] 
		return np.divide(ret, emoji_width*emoji_height)

	# the final image will have sizes multiples of the emoji dimensions
	final_height = emoji_height*(image_height//emoji_height)
	final_width = emoji_width*(image_width//emoji_width)

	ret = np.zeros((final_height, final_width, 3), dtype=np.uint8)

	start_time = dt.datetime.now()

	for i in range(0, final_height, emoji_height):
		for j in range(0, final_width, emoji_width):
			subgrid_mean = sub_mean(i, j)
			nearest_neighbor = search_tree.data[search_tree.query(tuple(subgrid_mean), p = 1)[1]]
			emoji = image_dict[tuple(nearest_neighbor)]
			ret[i:i+emoji_height, j:j+emoji_width, :] = emoji[:, :, :3]

	end_time = dt.datetime.now()

	print("Image construction: %f"%((end_time-start_time).microseconds/1e6))

	return ret

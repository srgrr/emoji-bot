import numpy as np
import datetime as dt

def img2emoji(image_content, image_dict, search_tree = None):
  '''Given a numpy.ndarray that represents an RGB image (with values in 0-255),
    a dictionary of the form {(R, G, B) : image} and, optionally, an scipy KD-Tree
    of the dictionary keys, creates an emoji-art image.
    If the KD-Tree is not specified it will be created
  '''
  start_time = dt.datetime.now()

  image_points = np.array([list(p) for p in image_dict.keys()])
  emoji_height, emoji_width, _ = image_dict[tuple(image_points[0])].shape
  if search_tree is None:
    from scipy.spatial import KDTree
    search_tree = KDTree(image_points)

  image_height, image_width, _ = image_content.shape

  def sub_mean(i, j):
    '''Compute the mean color of a subgrid [i, j] X [i + E - 1, i + E - 1].
    We have tried many approaches, and this one seems to be the one that
    works faster. Another possible approach is to compute partial prefix
    sums and output the means in O(1). For some reason, this works slower
    than explicit mean computation.
    '''
    ret = [0]*3
    for k in range(3):
      ret[k] = int(np.mean(image_content[i:i+emoji_height, j:j+emoji_width, k]))
    return tuple(ret)

  # The final image will have sizes multiples of the emoji dimensions
  # If the original image had non-multiple dimensions it will be truncated
  # ("ceiling padding" adds black pixels).
  final_height = emoji_height*(image_height//emoji_height)
  final_width = emoji_width*(image_width//emoji_width)

  ret = np.zeros((final_height, final_width, 3), dtype=np.uint8)

  for i in range(0, final_height, emoji_height):
    for j in range(0, final_width, emoji_width):
      subgrid_mean = sub_mean(i, j)
      # This search guarantees logarithmic complexity
      nearest_neighbor = search_tree.data[search_tree.query(tuple(subgrid_mean), p = 1)[1]]
      emoji = image_dict[tuple(nearest_neighbor)]
      ret[i:i+emoji_height, j:j+emoji_width, :] = emoji[:, :, :3]

  # Benchmarking data
  end_time = dt.datetime.now()
  print('Image construction: %.08f'%((end_time-start_time).microseconds/1e6))

  return ret

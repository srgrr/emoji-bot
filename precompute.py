import numpy as np
import random
import pickle
import glob
import sys
import os
from scipy import misc

def precompute(prefix_path):
  '''Precomputes the means of the images and then leaves
    a serialized dictionary of the form {mean : images},
    where images is a list of numpy matrices with shapes (w, h, 3)
  '''
  folder_name = os.path.split(prefix_path)[-1]
  precalc_path = os.path.join(os.path.split(sys.argv[0])[0], 'resources', 'precalc')
  if not os.path.exists(precalc_path):
    os.makedirs(precalc_path)

  images = glob.iglob(os.path.join(prefix_path, '*.png'))

  image_dict = {}

  for image in images:
    try:
      raw_array = misc.imread(image)
      for i in range(raw_array.shape[0]):
        for j in range(raw_array.shape[1]):
          res = sum(raw_array[i, j, k] for k in range(3))
          if res == 3*255:
            for k in range(3): raw_array[i, j, k] = 0 
      array_mean = []
      for k in range(3):
        array_mean.append(np.mean(raw_array[:, :, k]))
      array_mean = tuple(int(x) for x in array_mean)
      if not array_mean in image_dict or random.randint(0, 1) == 1:
        image_dict[array_mean] = raw_array
    except Exception as e:
	    pass

  pickle.dump(image_dict, open(os.path.join(precalc_path, folder_name), 'wb'))


def get_precomputed_dict(resource_name, force_comp = False):
  '''Returns a dict of the form {mean : image}.
    If we can find it serialized then it wont be computed again
    unless the parameter force_comp is set on True
  '''
  prefix_path = os.path.split(sys.argv[0])[0]
  file_name = os.path.join(prefix_path, 'resources', 'precalc', resource_name)
  if force_comp or not os.path.isfile(file_name):
    precompute(os.path.join(prefix_path, 'resources', resource_name))
  return pickle.load(open(file_name, 'rb'))

if __name__ == '__main__':
  get_precomputed_dict('emojis36', False)

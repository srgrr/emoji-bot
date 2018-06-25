from precompute import get_precomputed_dict
from img2emoji import img2emoji
from scipy import misc
import sys
import io

emoji_source = "emojis18"

def main():
  '''Small driver program.
  '''
  filename = sys.argv[1]
  print('Reading image')
  image_content = misc.imread(filename)
  print('Getting dict')
  dkt = get_precomputed_dict(emoji_source, True)
  print('Computing image')
  ret = img2emoji(image_content, dkt, None)
  print('Saving image')
  misc.imsave('result.png', ret)

if __name__ == "__main__":
  main()

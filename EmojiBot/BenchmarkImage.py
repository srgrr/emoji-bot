from scipy.misc import imread, imsave
from Emojifier import Emojifier


def benchmark_image(token, emoji_directory, scale, pattern):
    emojifier = Emojifier.create_from_directory(emoji_directory)
    emojified_image = emojifier.emojify_image(imread(token), scale, pattern)
    imsave('result.png', emojified_image)

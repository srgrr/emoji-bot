class Emojifier(object):

    def __init__(self, image_list):

        self.__images = image_list

        import numpy as np

        # Only RGB are important when considering the nearest image
        # Discard alphas
        means = \
            [
                tuple([int(np.mean(img[:, :, k])) for k in range(3)])
                for img in self.__images
            ]

        # Who cares about collisions lmao
        self.__mean_dict = dict(
            [
                (k, v) for (k, v)
                in zip(means, self.__images)
            ]
        )

        from scipy.spatial import KDTree
        self.__tree = KDTree(means)

    @staticmethod
    def create_from_directory(directory):
        import glob
        import os
        import imageio

        image_list = \
            [
                imageio.imread(image)
                for image in glob.glob(os.path.join(directory, '*'))
            ]

        return Emojifier(image_list)

    def emojify_image(self, image, scale, pattern_key='grid'):
        image_height = image.shape[0]
        image_width = image.shape[1]

        from math import sqrt

        emoji_height_ratio = \
            scale * sqrt(image_height) / float(self.__images[0].shape[0])

        emoji_height = int(self.__images[0].shape[0] * emoji_height_ratio)
        emoji_width = int(self.__images[0].shape[1] * emoji_height_ratio)

        result_height = \
            emoji_height * ((image_height + emoji_height - 1) // emoji_height)
        result_width = \
            emoji_width * ((image_width + emoji_width - 1) // emoji_width)

        from Pattern import PatternClassFactory
        pattern = PatternClassFactory.get_from_string(pattern_key)(
            result_height,
            result_width,
            emoji_height,
            emoji_width
        )

        import numpy as np

        ret = np.zeros((result_height, result_width, 4))

        for [t, l, b, r] in pattern.get_pattern_sequence():
            means = tuple(
                [
                    int(np.mean(image[t:b + 1, l:r + 1, k]))
                    for k in range(3)
                ]
            )

            nearest_mean = tuple(
                self.__tree.data[
                    self.__tree.query(means, p=1)[1]
                ]
            )

            from scipy import misc
            emoji = \
                misc.imresize(
                    self.__mean_dict[nearest_mean],
                    (emoji_height, emoji_width)
                )

            for k in range(3):
                # superposition rule: emoji has priority over image
                ret[t:b + 1, l:r + 1, k] = \
                    emoji[:, :, 3] / 255. * emoji[:, :, k] + \
                    (1.0 - emoji[:, :, 3] / 255.) * ret[t:b + 1, l:r + 1, k]

                ret[t:b + 1, l:r + 1, 3] = \
                    np.maximum(ret[t:b + 1, l:r + 1, 3], emoji[:, :, 3])

        ret[:, :, 3] = 255

        return ret

import numpy as np


class ImageError:
    """
    The image error function is an object that is responsible of
    calculating the difference between the objective image and
    the current canvas, this function can calculates the error
    of the image in total, it just provides an informative difference
    and it does not affect performance at all.
    """

    def error(self, original, generated):
        generated = generated[:, :, :3]
        mse = np.square(original - generated).mean()
        return mse


class IndividualImportance:
    """
    The individual error calculates the importance of a single
    individual. Instead of calculating the error, we calculate
    the importance, that is, how important an individuals contribution
    has in the image.
    """
    def error(self, sector):
        return sector.sum()

import numpy as np

class FitnessFunction:
    """
    The fitness function is an object that is responsible of
    calculating the difference between the objective image and
    the current canvas, this function can calculate the specific
    error of each individual to give the most accurate result.
    The individual error is save only for operators that eliminate
    brushes
    """

    def error(self, original, generated):
        mse = np.square(original - generated).mean()
        return mse

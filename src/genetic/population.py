import numpy as np


class PaintingPopulation:

    def __init__(self, objective, initial_size):
        self.objective = objective
        self.size = initial_size
        self.individuals = []

    def image(self):
        """
        Given all the individual brushes
        we can generate an image from all of them
        :return: image of brushes
        """
        canvas = np.ones(self.objective.shape)

        return canvas

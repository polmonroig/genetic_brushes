import numpy as np
from genetic.individual import IndividualBrush

class PaintingPopulation:

    def __init__(self, objective, initial_size):
        self.objective = objective
        self.size = initial_size
        self.individuals = []
        self.randomize()

    def randomize(self):
        for i in range(self.size):
            brush = IndividualBrush()
            brush.randomize()
            brush.set_color((0, 2, 0))
            self.individuals.append(brush)

    def image(self):
        """
        Given all the individual brushes
        we can generate an image from all of them
        :return: image of brushes
        """
        canvas = np.ones(self.objective.shape)
        canvas.fill(255)

        return canvas

import numpy as np
import cv2
from genetic.individual import IndividualBrush


class PaintingPopulation:
    """
    A population contains a lot of individuals, that act independently,
    this population updates over time and tries to improve to reach
    its objective. A population represents a canvas of that has the
    same shape as the objective shape, it is initially empty, but
    as the population changes, each individual applies a specific brush.
    A canvas is always changing, although it has has a memory of past
    generations of the population, many individuals may be destroyed
    between generations as consequence of specific operators, but their
    marks are still saved in the canvas

    Attributes:
    self.objective (matrix): original image to be painted, it is the objective
                             to which the algorithm must arrive
    self.size  (float): the initial size of the population
    self.canvas (matrix): represents the white image with all the brushes
    self.individuals (array): list of all the brushes in the canvas in the current generation
    """

    def __init__(self, objective, initial_size):
        self.objective = objective
        self.size = initial_size
        self.canvas = None
        self.individuals = []
        self.randomize()

    def randomize(self):
        for i in range(self.size):
            brush = IndividualBrush()
            brush.randomize()
            brush.set_color(np.array([0, 0, 0]))
            self.individuals.append(brush)

    def image(self):
        """
        Given all the individual brushes
        we can generate an image from all of them
        :return: image of brushes
        """
        if self.canvas is None:
            self.canvas = np.ones(self.objective.shape)
            self.canvas.fill(255)
        for ind in self.individuals:
            print("Loading image", ind.brush)
            image = cv2.imread(ind.brush)
            image = image * ind.color
            self.canvas[ind.pos[0]:ind.pos[1] + image.shape[0], ind.pos[0]:ind.pos[0] + image.shape[1]] = image
            self.canvas = image

        return self.canvas

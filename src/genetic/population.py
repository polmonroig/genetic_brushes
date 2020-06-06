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
            color = self.objective[brush.pos[1], brush.pos[0]] / 255.0
            brush.set_color(color)
            self.individuals.append(brush)

    def image(self):
        """
        Given all the individual brushes
        we can generate an image from all of them
        :return: image of brushes
        """
        if self.canvas is None:
            self.canvas = np.ones(self.objective.shape, dtype=np.uint8)
            self.canvas.fill(255)
        for ind in self.individuals:
            print("Loading image", ind.brush)
            image = cv2.imread(ind.brush)
            dim = (int(image.shape[0] * ind.size), int(image.shape[1] * ind.size))
            image = cv2.resize(image, dim)
            image = image * ind.color
            self.insert_image(ind.pos, image)

        return self.canvas

    def insert_image(self, pos, image):
        pos_x = pos[0]  # x == col
        pos_y = pos[1]  # y == row
        width = image.shape[1]
        height = image.shape[0]
        print("Inserting image of shape", image.shape, "at pos", pos)

        self.canvas[pos_y:pos_y + height, pos_x:pos_x + width] = image

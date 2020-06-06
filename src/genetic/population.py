import numpy as np
import cv2
from genetic.individual import IndividualBrush
from operators.operator import Mutation, Crossover, Selection


class PaintingPopulation:
    """
    A population contains a lot of individuals that act independently,
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
    self.operators (array): list of operators that are applied to the population on an update
    """

    def __init__(self, objective, initial_size):
        self.objective = objective
        self.size = initial_size
        self.canvas = None
        self.individuals = []
        self.randomize()
        self.operators = [Mutation(), Crossover(), Selection()]

    def update(self):
        # first apply operators
        for operator in self.operators:
            self.individuals = operator.op(self.individuals)
        # update colors
        for ind in self.individuals:
            color = self.objective[ind.pos[1], ind.pos[0]] / 255.0
            ind.set_color(color)

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
        width = image.shape[1]
        height = image.shape[0]
        pos_x = pos[0]  # x == col
        if pos_x >= self.canvas.shape[1] - width:
            pos_x = self.canvas.shape[1] - width
        pos_y = pos[1]  # y == row
        if pos_y >= self.canvas.shape[0] - height:
            pos_y = self.canvas.shape[0] - height
        alpha_image = image[:, :, 0] / 255.0
        alpha_canvas = 1.0 - alpha_image
        for c in range(0, 3):
            self.canvas[pos_y:pos_y + height, pos_x:pos_x + width, c] = (1 * image[:, :, c] +
                                      0 * self.canvas[pos_y:pos_y + height, pos_x:pos_x + width, c])



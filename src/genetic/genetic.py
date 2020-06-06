from population import PaintingPopulation
import cv2


class Genetic:
    """
    A genetic works by creating a brush population and iterating,
    until a painting condition is met (i.e. error is low enough).
    First, a random sample is generated from which different operators
    are applied, this operators modify the population by creating new
    individuals and destroying old ones.

    Attributes:
    self.objective (matrix): original image to be painted, it is the objective
                             to which the algorithm must arrive
    self.margin (float): the quantity of error that is accepted when searching
                         for a solution, it determines when will the algorithm
                         stop searching

    Static Variables:
    MAX_ITERATIONS (int): given that it is possible that the algorithm loops forever
                          we specify a limit
    """
    MAX_ITERATIONS = 100

    def __init__(self, objective, margin):
        self.objective = cv2.imread(objective)
        self.margin = margin

    def start(self):
        error = self.margin # allow first iteration
        it = 0
        population = PaintingPopulation()
        while it < Genetic.MAX_ITERATIONS and error >= self.margin:

            it += 1

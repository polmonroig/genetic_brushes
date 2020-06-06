from population import PaintingPopulation
import cv2


class Genetic:
    def __init__(self, objective):
        self.objective = cv2.imread(objective)

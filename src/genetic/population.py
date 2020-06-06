

class PaintingPopulation:

    def __init__(self, initial_size):
        self.size = initial_size
        self.individuals = []

    def image(self):
        """
        Given all the individual brushes
        we can generate an image from all of them
        :return: image of brushes
        """
        raise NotImplementedError("TODO")


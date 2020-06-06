

class IndividualBrush:
    """

    self.pos (pair): position of the brush relative to the painting
    self.direction (float): rotation degree of  the brush
    self.color (array): color of the brush
    self.brush (str): filename of the brush to paint
    self.size (float): relative size of the brush
    """
    def __init__(self):
        self.pos = (0, 0)
        self.direction = 0
        self.color = [0, 0, 0]
        self.brush = None
        self.size = 0

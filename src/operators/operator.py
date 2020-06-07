from genetic.individual import IndividualBrush


class Mutation:
    """
    The mutation operation selects traits of specific individuals and
    creates variations, this prevents local minimums and allows a the
    creation of new, unseen states
    """
    def op(self, individuals):
        """

        :param individuals: objects where the operation will be applied
        :return: list of resulting offsprings based on the operation
        """
        # limit min_size
        IndividualBrush.min_size -= 0.01
        IndividualBrush.max_size -= 0.01
        for ind in individuals:
            ind.randomize()
        return individuals


class Selection:
    """
    The selection operation trims specific individuals based on their
    superiority, a.k.a. survival of the fittest
    """
    def op(self, individuals):
        """

        :param individuals: objects where the operation will be applied
        :return: list of resulting offsprings based on the operation
        """
        return individuals


class Crossover:
    """
    The crossover operation selects series of individuals and tries to combine
    the best characteristic of each to create a much robust individual that
    adapts better to the canvas
    """
    def op(self, individuals):
        """

        :param individuals: parent objects where the operation will be applied
        :return: list of resulting offsprings based on the operation
        """
        return individuals
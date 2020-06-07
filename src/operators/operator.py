from genetic.individual import IndividualBrush


class Mutation:
    """
    The mutation operation selects traits of specific individuals and
    creates variations, this prevents local minimums and allows a the
    creation of new, unseen states
    """

    MIN_SIZE = 0.01

    def op(self, individuals):
        """

        :param individuals: objects where the operation will be applied
        :return: list of resulting offsprings based on the operation
        """
        # limit min_size
        if IndividualBrush.min_size >= Mutation.MIN_SIZE:
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
        return individuals[:int(len(individuals) * 0.6)]


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

        initial_size = len(individuals)
        for i in range(1, initial_size):
            individuals.append(IndividualBrush.merge(individuals[i - 1], individuals[i]))

        return individuals

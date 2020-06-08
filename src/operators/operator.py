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
        for ind in individuals:
            ind.randomize_item()
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
        individuals.sort()
        return individuals[:10]  # get individuals with more importance only


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
        increase = 2
        for j in range(increase):
            for i in range(1, initial_size):
                individuals.append(IndividualBrush.merge(individuals[i - 1], individuals[i]))

        return individuals

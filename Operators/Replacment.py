import GAutils
import Genome


def replacement_elitism(population, child1, child2, i):
    """
    This method search for the lest good solutions and replace them with the new solutions
    :param population: the population to work with
    :param child1: the first solution to push
    :param child2: the second solution to push
    :param i: the number of generation
    :return: the new population
    """
    pop = population.getPop()
    lst = population.get_2best_solution()
    best = lst[0]
    best2 = lst[1]
    index = 0
    if (i % 3) == 0:
        if child1.getFit() >= best[1]:
            first_child = child1
        else:
            first_child = Genome.Genome(pop[best[0]].zenith_angle, pop[best[0]].azimuth, pop[best[0]].best_angle, 0, 0, pop[best[0]].getSequence())
        if child2.getFit() >= best2[1]:
            second_child = child2
        else:
            second_child = Genome.Genome(pop[best2[0]].zenith_angle, pop[best2[0]].azimuth, pop[best2[0]].best_angle, 0, 0, pop[best2[0]].getSequence())
    else:
        first_child = child1
        second_child = child2
    min = pop[0].getFit()
    for i in range(GAutils.CONST_POPULATION_SIZE):
        if pop[i].getFit() < min:
            min = pop[i].getFit()
            index = i
    pop[index] = first_child
    index = 0
    min = pop[0].getFit()
    for i in range(GAutils.CONST_POPULATION_SIZE - 1):
        if pop[i].getFit() < min:
            min = pop[i].getFit()
            index = i
    pop[index] = second_child
    population.setPop(pop)
    return population

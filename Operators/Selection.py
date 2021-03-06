import random
import GAutils


def rouletteSelection(population):
    """
    This function takes the population - all of the solutions and divide it into slices of a pie,
    each pie size is depends on the fitness of the solution based on its penalty, the bigger the slice
    the bigger the chance for the solution to be chose.
    :param population: the population to work with
    :return: 2 solutions randomly chosen
    """
    chosen = []
    genes = population.getPop()
    count = 0
    while count < 2:
        temp = random.uniform(0, population.getFitnessProb())
        for gene in genes:
            rangee = gene.getRange()
            max = rangee[1]
            min = rangee[0]
            if max > temp > min:
                if count == 0:
                    chosen.append(gene)
                    count += 1
                else:
                    if chosen[0] != gene:
                        chosen.append(gene)
                        count += 1
    return chosen

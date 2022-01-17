import GAutils
import random
import Genome


def crossover(chrom1: Genome, chrom2: Genome):
    """
    This method takes two parents solution and cross them in order to get a new solution
    :param chrom1: the first parents solution
    :param chrom2: the second parents solution
    :return: the newborn solutions
    """
    position = random.randint(0, GAutils.CONST_SEQUENCE_LENGTH)
    child1 = chrom1.getSequence()[0:position]
    child2 = chrom2.getSequence()[0:position]
    child1 = child1 + chrom2.getSequence()[position:]
    child2 = child2 + chrom1.getSequence()[position:]
    child1 = Genome.Genome(chrom1.zenith_angle, chrom1.azimuth, chrom1.best_angle, 0, 0, child1)
    child2 = Genome.Genome(chrom2.zenith_angle, chrom2.azimuth, chrom2.best_angle, 0, 0, child2)
    child1.evaluate()
    child2.evaluate()
    offspring = [child1, child2]
    return offspring

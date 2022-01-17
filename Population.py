import Genome
import GAutils
import numpy
import datetime


class Population:
    """
    Class to describe the population
    """
    pop_size = 0
    fitness = 0
    latitude = 0
    longtitude = 0
    azimuth = 0
    cell_length = 0
    cell_width = 0
    zenith_angle = 0
    declimination_angle = 0
    best_angle = 0
    area = 0

    def __init__(self):
        """
        initialize the empty population
        """
        Population.pop_size = 0
        Population.fitness = 0
        self.pop = []
        self.fitnessProbs = 0

    def createInitial(self, size):
        """
        This method builds the population
        :param size: the size of the population
        :return: NONE
        """
        self.pop_size = size
        self.calculate_declimination_angle()
        self.calculate_zenith_angle()
        self.calculate_best_angle()
        for i in range(size):
            a = Genome.Genome(self.zenith_angle, self.azimuth, self.best_angle, self.cell_length, self.cell_width)
            a.evaluate()
            self.pop.append(a)
            self.fitness += a.fitness

    def update_fitness(self):
        """
        update the fitness of each chromosome in the population
        :return: NONE
        """
        self.fitness = 0
        pop = self.pop
        for chromosome in pop:
            self.fitness += chromosome.fitness

    def get_chromosome_by_index(self, index):
        """
        This method returns a requested solution from the population
        :param index: the requested index
        :return: the requested solution
        """
        pop = self.getPop()
        for i in range(GAutils.CONST_POPULATION_SIZE):
            if i == index:
                return pop[i]

    def getFitness(self):
        """
        This method returns the population Fitness
        :return: population fit
        """
        return abs(self.fitness)

    def getPop(self):
        """
        This method returns the population
        :return: the population
        """
        return self.pop

    def updateGenesRange(self):
        """
        This method updates the solution ranges for the roulette selection
        :return: NONE
        """
        genes = self.getPop()
        totalFit = self.fitness
        min = 0
        max = 0
        for i in range(genes.__len__()):
            max += (genes[i].getFit() / totalFit)
            genes[i].setRange(min, max)
            min = max
        self.setPop(genes)
        self.fitnessProbs = min

    def getFitnessProb(self):
        """
        This method returns fitness probability
        :return: fitness probability
        """
        return self.fitnessProbs

    def setPop(self, pop):
        """
        This method sets the population
        :param pop:
        :return: NONE
        """
        self.pop = pop

    def get_best_solution(self):
        """
        This method checks the best solution in the population
        :return: The best solution
        """
        index = 0
        max = 0
        pop = self.pop
        for i in range(GAutils.CONST_POPULATION_SIZE):
            if pop[i].getFit() > max:
                max = pop[i].getFit()
                index = i
        lst = [index, max]
        return lst

    def get_2best_solution(self):
        """
        This method checks the two best solutions in the population
        :return: list of the two best solutions
        """
        index = 0
        max = 0
        second_max = 0
        index_2 = 0
        pop = self.pop
        for i in range(GAutils.CONST_POPULATION_SIZE):
            if pop[i].getFit() > max:
                second_max = max
                max = pop[i].getFit()
                index_2 = index
                index = i
            elif pop[i].getFit() > second_max:
                second_max = pop[i].getFit()
                index_2 = i
        temp_lst = [index, max]
        temp_2lst = [index_2, second_max]
        lst = []
        lst.append(temp_lst)
        lst.append(temp_2lst)
        return lst

    def calculate_declimination_angle(self):
        """
        This method calc's declination angle
        :return: NONE
        """
        date = datetime.datetime.today()
        days = ((date.month - 1) * 30) + date.day
        sin_dec_angle = 0.39795 * numpy.cos(numpy.deg2rad(0.98563 * (days-173)))
        dec_angle_temp = numpy.arcsin(sin_dec_angle)
        dec_angle = numpy.rad2deg(dec_angle_temp)
        self.declimination_angle = dec_angle

    def calculate_zenith_angle(self):
        """
        This method calc's the zenith angle
        :return: NONE
        """
        self.zenith_angle = self.latitude - self.declimination_angle

    def calculate_best_angle(self):
        """
        This method calc's the best angle of the cell slope
        :return: NONE
        """
        date = datetime.datetime.today()
        if date.month >= 11 or date.month < 4:
            self.best_angle = (self.latitude * 0.9) + 29
        else:
            self.best_angle = (self.latitude * 0.9) - 23.5

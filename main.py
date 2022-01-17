import GAutils
import Population
from Operators import Crossover, Selection, Replacment, Mutation
import time
from matplotlib import pyplot

POP_NUM = 1


def main_run(init_pop):
    """
    The main algorithm, actually runs the Genetic Algorithm and gives results
    :param init_pop: Our population
    :return: sol_lst: list that contains the best solution in first place and fitness avg in second
    """
    start_time = time.time()
    print(time.time())
    fitness_lst = []
    best_sol_total = 0
    total_fit = 0
    for j in range(POP_NUM):
        index_lst = []
        pop = Population.Population()
        pop.latitude = init_pop.latitude
        pop.longtitude = init_pop.longtitude
        pop.azimuth = init_pop.azimuth
        pop.cell_length = init_pop.cell_length
        pop.cell_width = init_pop.cell_width
        pop.createInitial(GAutils.CONST_POPULATION_SIZE)
        temp = []
        lst = []
        best_at_each_generation = []
        for i in range(GAutils.CONST_GENERATIONS):
            pop.updateGenesRange()
            best = pop.get_best_solution()
            if i == 0:
                temp.append(pop.get_chromosome_by_index(best[0]).getSequence())
                temp.append(best[1])
                lst.append(temp)
                temp = []
                best_sol_total = pop.get_chromosome_by_index(best[0])
                total_fit += pop.getFitness()
            child_created = []
            for k in range(GAutils.CONST_POPULATION_SIZE // 2):
                selected = Selection.rouletteSelection(pop)
                offspring = Crossover.crossover(selected[0], selected[1])
                c1 = offspring[0]
                c2 = offspring[1]
                c1 = Mutation.mutate(c1)
                c2 = Mutation.mutate(c2)
                child_created.append(c1)
                child_created.append(c2)
            for k in range(GAutils.CONST_POPULATION_SIZE // 2):
                pop = Replacment.replacement_elitism(pop, child_created[k * 2], child_created[k * 2 + 1], i)
            pop.update_fitness()
            best = pop.get_best_solution()
            if i == (GAutils.CONST_GENERATIONS - 1):
                temp.append(pop.get_chromosome_by_index(best[0]).getSequence())
                temp.append(best[1])
                lst.append(temp)
            best_at_each_generation.append(best[1])
            fitness_lst.append(pop.getFitness())
            index_lst.append(i)
            total_fit += pop.getFitness()
            if best[1] > best_sol_total.getFit():
                best_sol_total = pop.get_chromosome_by_index(best[0])
    print(time.time() - start_time)
    print('im after 2 populations')
    sol_lst = [best_sol_total, total_fit / GAutils.CONST_GENERATIONS]
    return sol_lst



from Chromosome import Chromosome
from Population import Population
from proj1 import constants

if __name__ == '__main__':
    pop = Population(population_count=50, max_range=5, min_range=-5, value_func_name=constants.STYBLISNKI_TANG_FUNCTION,
                     selection_name=constants.BEST,
                     selection_param=4, is_maximization=False, crossover_name=constants.ONE_POINT, crossover_param=0.5,
                     mutation_name=constants.TWO_POINT, mutation_param=0, inversion_param=1, has_elitism=True,
                     elitism_count=2, epochs=300, genes_count=2)

    value = pop.population_loop()
    print(value)

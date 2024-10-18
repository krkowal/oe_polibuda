from Chromosome import Chromosome
from constants import GENS_COUNT_DIR, VALUE_FUNC_DIR
from Selection import Selection
from proj1.Crossover import Crossover
from proj1.Inversion import Inversion
from proj1.Mutation import Mutation


class Population:

    def __init__(self, population_count, value_func_name, min_range, max_range, selection_name, selection_param,
                 crossover_name, crossover_param, mutation_name, mutation_param, inversion_param, has_elitism=False,
                 elitism_count=0,
                 is_maximization=False):
        self._is_maximization = is_maximization
        self._population_count = population_count
        self._value_func_name = value_func_name
        self._value_func = VALUE_FUNC_DIR[value_func_name]
        self._gens_count = GENS_COUNT_DIR[value_func_name]
        self._min_range = min_range
        self._max_range = max_range
        self._selection = Selection(selection_name, selection_param, has_elitism=has_elitism,
                                    elitism_count=elitism_count, is_maximization=is_maximization)
        self._crossover = Crossover(crossover_name, population_count, crossover_param, elite_count=elitism_count)
        self._mutation = Mutation(mutation_name, mutation_param)
        self._inversion = Inversion(inversion_param)
        self._has_elitism = has_elitism
        self._elitism_count = elitism_count
        self._chromosomes_list = [Chromosome(gens_count=self._gens_count, min_range=min_range, max_range=max_range) for
                                  _ in range(population_count)]

    def evaluate_chromosomes(self):
        return list(zip(self._chromosomes_list,
                        list(map(lambda chromosome: chromosome.get_value(self._value_func), self._chromosomes_list))))

    def population_loop(self):
        selected_chromosomes_list = self._selection.select(self.evaluate_chromosomes())
        elite_chromosomes_list = []
        if self._has_elitism:
            elite_chromosomes_list = selected_chromosomes_list[:self._elitism_count]
            selected_chromosomes_list = selected_chromosomes_list[self._elitism_count:]

        crossed_chromosome_list = self._crossover.cross(selected_chromosomes_list)

        crossed_chromosome_list = crossed_chromosome_list[:self._population_count - self._elitism_count]
        mutated_chromosomes_list = self._mutation.mutate(crossed_chromosome_list)

        inverted_chromosomes = self._inversion.invert(mutated_chromosomes_list)

        elite_chromosomes_list.extend(inverted_chromosomes)
        self._chromosomes_list = elite_chromosomes_list

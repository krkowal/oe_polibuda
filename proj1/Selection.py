import math
import random
from operator import itemgetter
from proj1 import constants
from Chromosome import Chromosome


def get_sorted_chromosome_values(chromosome_list, is_reversed):
    return sorted(chromosome_list, key=itemgetter(1), reverse=is_reversed)


class Selection:

    def __init__(self, selection_name, param, has_elitism=False,
                 elitism_count=0, is_maximization=False):
        self.__selection_count = None
        self.__current_chromosome_list = None
        self.SELECTION_FUNC_DIR = {
            constants.BEST: self.best_selection
            , constants.ROULETTE: self.roulette
            , constants.TOURNAMENT: self.tournament
        }
        self._is_maximization = is_maximization
        self._param = param
        self._selection_func = self.SELECTION_FUNC_DIR[selection_name]
        self._has_elitism = has_elitism
        self._elitism_count = elitism_count

    def best_selection(self) -> list[Chromosome]:
        sorted_chromosome_list = get_sorted_chromosome_values(self.__current_chromosome_list,
                                                              is_reversed=self._is_maximization)
        # print(sorted_chromosome_list)
        return sorted_chromosome_list[:self._param - self._elitism_count]

    def roulette(self) -> set[Chromosome]:
        fitness_values = [value for chromosome, value in self.__current_chromosome_list] if self._is_maximization else [
            1 / value for chromosome, value in self.__current_chromosome_list]
        total_fitness = sum(fitness_values)
        relative_fitness = [fitness / total_fitness for fitness in fitness_values]
        cumulative_probabilities = []
        cumulative_sum = 0
        for rf in relative_fitness:
            cumulative_sum += rf
            cumulative_probabilities.append(cumulative_sum)

        selected_chromosomes = set()
        # print(self.__current_chromosome_list)
        # print(cumulative_probabilities)
        while len(selected_chromosomes) < self._param - self._elitism_count:
            random_value = random.random()
            # print(random_value)
            for i, cumulative_probability in enumerate(cumulative_probabilities):
                if random_value < cumulative_probability:
                    # Return the chromosome part of the tuple (chromosome_object, value)
                    selected_chromosomes.add(self.__current_chromosome_list[i])
                    break
        return selected_chromosomes

    def tournament(self) -> list[Chromosome]:
        random.shuffle(self.__current_chromosome_list)
        groups_list = [self.__current_chromosome_list[i:i + self._param] for i in
                       range(0, len(self.__current_chromosome_list), self._param)]
        # for group in groups_list:
        #     print("Group" + str(group))
        winner_chromosome_list = [group[0] for group in
                                  [get_sorted_chromosome_values(shuffled_group, is_reversed=self._is_maximization) for
                                   shuffled_group in groups_list]]

        return winner_chromosome_list

    def select(self, chromosome_list):
        if self._has_elitism:
            sorted_chromosomes_list = get_sorted_chromosome_values(chromosome_list, self._is_maximization)
            elite_chromosomes_list = sorted_chromosomes_list[:self._elitism_count]
            self.__current_chromosome_list = sorted_chromosomes_list[self._elitism_count:]
            elite_chromosomes_list.extend(self._selection_func())
            return elite_chromosomes_list
        else:
            self.__current_chromosome_list = chromosome_list
            return self._selection_func()

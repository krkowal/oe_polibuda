from abc import ABC, abstractmethod
from operator import itemgetter


def get_sorted_chromosome_values(chromosome_list, is_reversed):
    return sorted(chromosome_list, key=itemgetter(1), reverse=is_reversed)


class Selection(ABC):

    def __init__(self, has_elitism=False, elitism_count=0, is_maximization=False):
        
        self.__current_chromosome_list = None

        self._is_maximization = is_maximization
        self._has_elitism = has_elitism
        self._elitism_count = elitism_count

    def select(self, chromosome_list):
        if self._has_elitism:
            sorted_chromosomes_list = get_sorted_chromosome_values(chromosome_list, self._is_maximization)
            elite_chromosomes_list = sorted_chromosomes_list[:self._elitism_count]
            self.__current_chromosome_list = sorted_chromosomes_list[self._elitism_count:]
            elite_chromosomes_list.extend(self.selection_function())
            return elite_chromosomes_list
        else:
            self.__current_chromosome_list = chromosome_list
            return self.selection_function()

    @abstractmethod
    def selection_function(self):
        pass

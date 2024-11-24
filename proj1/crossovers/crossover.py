from abc import ABC, abstractmethod
import random

from proj1.chromosomes.binary import BinaryChromosome


class Crossover(ABC):

    def __init__(self, population_count, elite_count):
        self._population_count = population_count - elite_count

    def cross(self, chromosome_with_values_list: list[tuple[BinaryChromosome, float]]):
        current_chromosomes_list: list[BinaryChromosome] = [chromosome for chromosome, value in
                                                            chromosome_with_values_list]
        new_chromosomes_list = []
        while len(new_chromosomes_list) < self._population_count:
            new_chromosomes_list.extend(self._crossover_function(random.sample(current_chromosomes_list, 2)))
        return new_chromosomes_list

    @abstractmethod
    def _crossover_function(self, chromosome_list: list[BinaryChromosome]) -> list[BinaryChromosome]:
        pass

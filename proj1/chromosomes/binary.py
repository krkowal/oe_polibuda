from random import randint
from math import log2, ceil
from typing import List

from proj1.chromosomes.chromosome import Chromosome
from proj1.constants import ACCURACY


def calculate_gens_length(gen_range, accuracy):
    return ceil(log2(gen_range * 10 ** accuracy) + log2(1))


class BinaryChromosome(Chromosome):
    def __init__(self, gens_count, min_range, max_range, gens_length=None, gens=None):
        super().__init__(min_range, max_range)
        self._gen_range = max_range - min_range
        self._gens_count = gens_count
        self._gens_length = calculate_gens_length(self._gen_range, ACCURACY) if gens is None else gens_length
        self._gens_list = ["".join([str(randint(0, 1)) for _ in range(self._gens_length)]) for _ in
                           range(gens_count)] if gens is None else gens

    def get_variables_values(self) -> list[float]:
        return list(map(lambda gen: self._min_range + int(gen, 2) * self._gen_range / (2 ** self._gens_length - 1),
                        self._gens_list))

    @classmethod
    def from_crossover_and_mutations(cls, parent_chromosome: 'BinaryChromosome',
                                     genes_list: List[str]) -> 'BinaryChromosome':
        return cls(*parent_chromosome.get_init_params(), genes_list)

    def get_value(self, func) -> float:
        return func(self.get_variables_values())

    def __str__(self):
        decoded_values = self.get_variables_values()
        genes_with_values = [f"Gen: {gen}, Value: {value}" for gen, value in zip(self._gens_list, decoded_values)]
        return "\n".join(genes_with_values)

    def get_init_params(self):
        return [self._gens_count, self._min_range, self._max_range, self._gens_length]

    def get_genes_list(self) -> list[str]:
        return self._gens_list

    def get_gens_length(self) -> int:
        return self._gens_length

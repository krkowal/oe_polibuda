from proj1.chromosomes.chromosome import Chromosome
import random


class RealChromosome(Chromosome):
    def __init__(self, gens_count, min_range, max_range, genes=None):
        super().__init__()
        self._min_range = min_range
        self._max_range = max_range
        self._gen_range = max_range - min_range
        self._gens_count = gens_count

        self._gens_list = genes if genes else self.__get_random_genes()

    def get_value(self, func) -> float:
        return func(self._gens_list)

    def __get_random_genes(self):
        return [random.randrange(self._min_range, self._max_range) for _ in range(self._gens_count)]

    @classmethod
    def from_crossover_and_mutations(cls, parent_chromosome: 'RealChromosome', genes):
        return cls(*parent_chromosome.get_init_params(), genes)

    def get_init_params(self):
        return [self._gens_count, self._min_range, self._max_range]

from abc import ABC, abstractmethod


class Chromosome(ABC):

    def __init__(self, min_range, max_range):
        self._min_range = min_range
        self._max_range = max_range

    @abstractmethod
    def get_value(self, func) -> float:
        pass

    @abstractmethod
    def get_genes_list(self) -> list[str]:
        pass

    @classmethod
    @abstractmethod
    def from_crossover_and_mutations(cls, chromosome, new_genes):
        pass

    @property
    def min_range(self):
        return self._min_range

    @property
    def max_range(self):
        return self._max_range



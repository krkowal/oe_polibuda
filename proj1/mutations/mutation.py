import random
from abc import ABC, abstractmethod

from proj1.chromosomes.chromosome import Chromosome


class Mutation(ABC):

    @abstractmethod
    def mutate(self, chromosomes_list) -> list[Chromosome]:
        pass

    @abstractmethod
    def mutation_function(self, gene):
        pass

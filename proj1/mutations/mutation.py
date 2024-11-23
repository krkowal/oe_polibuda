import random
from abc import ABC, abstractmethod

from proj1.Chromosome import Chromosome


class Mutation(ABC):

    def __init__(self, mutation_param):
        self._mutation_param = mutation_param

    def mutate(self, chromosomes_list) -> list[Chromosome]:
        new_chromosomes = []
        for chromosome in chromosomes_list:
            new_genes = []
            for gene in chromosome.get_genes_list():
                rand_value = random.random()
                if rand_value < self._mutation_param:
                    new_genes.append(self.mutation_function(gene))
                else:
                    new_genes.append(gene)
            new_chromosomes.append(Chromosome.from_crossover_and_mutations(chromosome, new_genes))

        return new_chromosomes

    @abstractmethod
    def mutation_function(self, gene):
        pass

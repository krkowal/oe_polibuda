from proj1.Chromosome import Chromosome
from proj1.crossovers.crossover import Crossover
import random


class DiscreteCrossover(Crossover):
    def __init__(self, population_count, crossover_param, elite_count=0):
        super().__init__(population_count, elite_count)
        self._crossover_param = crossover_param

    def _crossover_function(self, chromosome_list: list[Chromosome]) -> list[Chromosome]:
        new_genes = []
        first_chromosome = chromosome_list[0]
        second_chromosome = chromosome_list[1]
        for gene_one, gene_two in zip(first_chromosome.get_genes_list(), second_chromosome.get_genes_list()):
            new_gene = ""
            for first, second in zip(gene_one, gene_two):
                random_p = random.random()
                if random_p <= self._crossover_param:
                    new_gene += first
                else:
                    new_gene += second
            new_genes.append(new_gene)
        return [Chromosome.from_crossover_and_mutations(first_chromosome, new_genes)]

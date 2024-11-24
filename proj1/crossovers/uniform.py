from proj1.chromosomes.binary import BinaryChromosome
from proj1.crossovers.crossover import Crossover
import random


class UniformCrossover(Crossover):
    def __init__(self, population_count, crossover_param, elite_count=0):
        super().__init__(population_count, elite_count)
        self._crossover_param = crossover_param

    def _crossover_function(self, chromosome_list: list[BinaryChromosome]) -> list[BinaryChromosome]:
        new_genes_first = []
        new_genes_second = []
        first_chromosome = chromosome_list[0]
        second_chromosome = chromosome_list[1]
        for gene_one, gene_two in zip(first_chromosome.get_genes_list(), second_chromosome.get_genes_list()):
            new_first_gene = ""
            new_second_gene = ""
            for first, second in zip(gene_one, gene_two):
                random_p = random.random()
                if random_p > self._crossover_param:
                    new_first_gene += first
                    new_second_gene += second
                else:
                    new_first_gene += second
                    new_second_gene += first
            new_genes_first.append(new_first_gene)
            new_genes_second.append(new_second_gene)

        return [BinaryChromosome.from_crossover_and_mutations(parent_chromosome=first_chromosome,
                                                              genes_list=new_genes_first),
                BinaryChromosome.from_crossover_and_mutations(parent_chromosome=first_chromosome,
                                                              genes_list=new_genes_second)]

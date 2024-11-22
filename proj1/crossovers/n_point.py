from abc import ABC, abstractmethod
from random import random

from proj1.Chromosome import Chromosome
from proj1.crossovers.crossover import Crossover


class NPointCrossover(Crossover, ABC):

    def __init__(self, population_count, elite_count=0):
        super().__init__(population_count, elite_count)

    def n_point_crossover(self, chromosome_list: list[Chromosome], n) -> list[Chromosome]:
        new_genes_first = []
        new_genes_second = []
        first_chromosome = chromosome_list[0]
        second_chromosome = chromosome_list[1]
        for gene_one, gene_two in zip(first_chromosome.get_genes_list(), second_chromosome.get_genes_list()):
            crossover_points = set()
            while len(crossover_points) < n:
                crossover_points.add(random.randint(0, first_chromosome.get_gens_length()))
            sorted_crossover_points = sorted(crossover_points)
            i = 0
            offset = 0
            new_first_gene = ""
            new_second_gene = ""
            for point in sorted_crossover_points:
                if i % 2 == 0:
                    new_first_gene += gene_one[offset:point]
                    new_second_gene += gene_two[offset:point]
                else:
                    new_first_gene += gene_two[offset:point]
                    new_second_gene += gene_one[offset:point]
                offset = point
                i += 1
            if i % 2 == 0:
                new_first_gene += gene_one[offset:]
                new_second_gene += gene_two[offset:]
            else:
                new_first_gene += gene_two[offset:]
                new_second_gene += gene_one[offset:]

            new_genes_first.append(new_first_gene)
            new_genes_second.append(new_second_gene)

        return [Chromosome.from_crossover_and_mutations(parent_chromosome=first_chromosome, genes_list=new_genes_first),
                Chromosome.from_crossover_and_mutations(parent_chromosome=first_chromosome,
                                                        genes_list=new_genes_second)]

    @abstractmethod
    def _crossover_function(self, chromosome_list: list[Chromosome]) -> list[Chromosome]:
        pass

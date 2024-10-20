import random
from typing import List, Callable

from proj1 import constants
from proj1.Chromosome import Chromosome


class Crossover:
    def __init__(self, crossover_name, population_count, crossover_param, elite_count=0):
        self._crossover_name = crossover_name
        self._population_count = population_count - elite_count
        self._crossover_param = crossover_param
        CROSSOVER_FUNC_DIR: dir[str, Callable[[list[Chromosome]], list[Chromosome]]] = {
            constants.ONE_POINT: self._one_point_crossover
            , constants.TWO_POINT: self._two_point_crossover
            , constants.UNIFORM: self._uniform_crossover, constants.DISCRETE: self._discrete_crossover
        }
        self._crossover_func = CROSSOVER_FUNC_DIR[crossover_name]

    def cross(self, chromosome_with_values_list: list[tuple[Chromosome, float]]):
        current_chromosomes_list: list[Chromosome] = [chromosome for chromosome, value in chromosome_with_values_list]
        new_chromosomes_list = []
        while len(new_chromosomes_list) < self._population_count:
            new_chromosomes_list.extend(self._crossover_func(random.sample(current_chromosomes_list, 2)))
        return new_chromosomes_list

    def _one_point_crossover(self, chromosome_list: list[Chromosome]) -> list[Chromosome]:
        return self.__n_point_crossover(chromosome_list, 1)

    def _two_point_crossover(self, chromosome_list: list[Chromosome]) -> list[Chromosome]:
        return self.__n_point_crossover(chromosome_list, 2)

    def __n_point_crossover(self, chromosome_list: list[Chromosome], n) -> list[Chromosome]:
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

    def _uniform_crossover(self, chromosome_list: list[Chromosome]) -> list[Chromosome]:
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

        return [Chromosome.from_crossover_and_mutations(parent_chromosome=first_chromosome, genes_list=new_genes_first),
                Chromosome.from_crossover_and_mutations(parent_chromosome=first_chromosome,
                                                        genes_list=new_genes_second)]

    def _discrete_crossover(self, chromosome_list: list[Chromosome]) -> list[Chromosome]:
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

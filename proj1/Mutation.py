import random

from proj1 import constants
from proj1.Chromosome import Chromosome


class Mutation:
    def __init__(self, mutation_name, mutation_param):
        self._mutation_name = mutation_name
        self._mutation_param = mutation_param

        MUTATION_FUNC_DIR = {
            constants.ONE_POINT: self._one_point_mutation
            , constants.TWO_POINT: self._two_point_mutation
            , constants.BOUNDARY: self._boundary_mutation
        }
        self._mutation_func = MUTATION_FUNC_DIR[mutation_name]

    def _one_point_mutation(self, gene):
        return self.__n_point_mutation(gene, 1)

    def _two_point_mutation(self, gene):
        return self.__n_point_mutation(gene, 2)

    def __n_point_mutation(self, gene, n, position_set=None):
        binary_list = list(gene)

        if position_set is None:
            mutation_points = set()
            while len(mutation_points) < n:
                mutation_points.add(random.randint(0, len(gene) - 1))
        else:
            mutation_points = position_set

        for point in mutation_points:
            binary_list[point] = '1' if binary_list[point] == '0' else '0'
        return "".join(binary_list)

    def _boundary_mutation(self, gene):
        position = {random.randint(0, 1) - 1}
        return self.__n_point_mutation(gene, 1, position_set=position)

    def mutate(self, chromosomes_list):
        new_chromosomes = []
        for chromosome in chromosomes_list:
            new_genes = []
            for gene in chromosome.get_genes_list():
                rand_value = random.random()
                if rand_value < self._mutation_param:
                    new_genes.append(self._mutation_func(gene))
                else:
                    new_genes.append(gene)
            new_chromosomes.append(Chromosome.from_crossover_and_mutations(chromosome, new_genes))

        return new_chromosomes

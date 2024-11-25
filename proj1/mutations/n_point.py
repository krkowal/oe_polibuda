import random
from abc import ABC

from proj1.mutations.binary_mutation import BinaryMutation


class NPointMutation(BinaryMutation, ABC):
    def __init__(self, mutation_param):
        super().__init__(mutation_param)

    def n_point_mutation(self, gene, n, position_set=None) -> str:
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

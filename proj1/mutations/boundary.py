import random

from proj1.mutations.n_point import NPointMutation


class BoundaryMutation(NPointMutation):

    def __init__(self, mutation_param):
        super().__init__(mutation_param)

    def mutation_function(self, gene):
        position = {random.randint(0, 1) - 1}
        return self.n_point_mutation(gene, 1, position_set=position)

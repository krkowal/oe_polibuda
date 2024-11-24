from proj1.mutations.n_point import NPointMutation


class TwoPointMutation(NPointMutation):
    def __init__(self, mutation_param):
        super().__init__(mutation_param)

    def mutation_function(self, gene):
        return self.n_point_mutation(gene, 2)

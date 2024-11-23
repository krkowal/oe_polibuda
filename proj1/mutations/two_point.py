from proj1.mutations.n_point import NPointMutation


class TwoPointMutation(NPointMutation):
    def mutation_function(self, gene):
        return self.n_point_mutation(gene, 2)

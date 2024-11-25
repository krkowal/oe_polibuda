from proj1.mutations.real_mutation import RealMutation
import numpy as np


class GaussMutation(RealMutation):
    def __init__(self, mutation_param):
        super().__init__(mutation_param)

    def mutation_function(self, chromosome):
        new_genes = []
        for gene in chromosome.get_genes_list():
            while True:
                normal_rand_value = np.random.normal(0, 1)
                print(gene, normal_rand_value)
                if chromosome.min_range <= gene + normal_rand_value <= chromosome.max_range:
                    new_genes.append(gene + normal_rand_value)
                    break

        return new_genes

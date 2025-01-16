import benchmark_functions
import numpy as np

from proj1 import constants


def one_point_mutation(offspring, ga_instance):
    pass

def uniform_mutation(offspring, ga_instance):
    for child in offspring:
        position = np.random.randint(0, len(child))
        child[position] = np.random.uniform(ga_instance.gene_space[position][0],
                                             ga_instance.gene_space[position][1])
    return offspring

def gaussian_mutation(offspring, ga_instance):
    for child in offspring:
        for idx in range(len(child)):
            while True:
                normal_rand_value = np.random.normal(0, 1)
                new_gene_value = child[idx] + normal_rand_value
                if ga_instance.gene_space[idx][0] <= new_gene_value <= ga_instance.gene_space[idx][1]:
                    child[idx] = new_gene_value
                    break
    return offspring

class PygadMutationFactory:
    @staticmethod
    def get_mutation(name):
        match name:
            case constants.ONE_POINT:
                return OnePointMutation(mutation_param)
            case constants.TWO_POINT:
                return TwoPointMutation(mutation_param)
            case constants.BOUNDARY:
                return BoundaryMutation(mutation_param)
            case constants.UNIFORM:
                return uniform_mutation
            case constants.GAUSS:
                return gaussian_mutation
            case _:
                raise ValueError(f"Unknown selection method: {name}")

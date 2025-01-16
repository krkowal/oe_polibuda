import benchmark_functions
import numpy as np

from proj1 import constants


def one_point_mutation(offspring, ga_instance):
    pass

def uniform_mutation(offspring, ga_instance):
    init_range_low = ga_instance.init_range_low
    init_range_high = ga_instance.init_range_high

    for chromosome_idx in range(offspring.shape[0]):
        genotype = offspring[chromosome_idx]
        position = np.random.choice(range(genotype.shape[0]))
        genotype[position] = np.random.uniform(init_range_low, init_range_high)

    return offspring

def gaussian_mutation(offspring, ga_instance):
    init_range_low = ga_instance.init_range_low
    init_range_high = ga_instance.init_range_high

    for chromosome_idx in range(offspring.shape[0]):
        genotype = offspring[chromosome_idx]
        new_genes = []

        for gene in genotype:
            max_attempts = 1000
            for _ in range(max_attempts):
                normal_rand_value = np.random.normal(0, 1)
                if init_range_low <= gene + normal_rand_value <= init_range_high:
                    new_genes.append(gene + normal_rand_value)
                    break
            else:
                new_genes.append(gene)

        offspring[chromosome_idx] = new_genes

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

import benchmark_functions
import numpy as np

from proj1 import constants


def one_point_mutation(offspring, ga_instance):
    for offspring_idx in range(offspring.shape[0]):
        if np.random.rand() > ga_instance.mutation_probability:
            continue
        mutation_point = np.random.randint(0, offspring.shape[1])
        offspring[offspring_idx, mutation_point] = 1 - offspring[offspring_idx, mutation_point]

    return offspring


def two_point_mutation(offspring, ga_instance):
    for offspring_idx in range(offspring.shape[0]):
        if np.random.rand() > ga_instance.mutation_probability:
            continue
        for i in range(2):
            mutation_point = np.random.randint(0, offspring.shape[1])
            offspring[offspring_idx, mutation_point] = 1 - offspring[offspring_idx, mutation_point]

    return offspring


def boundary_mutation(offspring, ga_instance):
    for offspring_idx in range(offspring.shape[0]):
        if np.random.rand() > ga_instance.mutation_probability:
            continue
        mutation_point = np.random.randint(0, 1) * offspring.shape[1]
        offspring[offspring_idx, mutation_point] = 1 - offspring[offspring_idx, mutation_point]

    return offspring


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
                return one_point_mutation
            case constants.TWO_POINT:
                return two_point_mutation
            case constants.BOUNDARY:
                return boundary_mutation
            case constants.UNIFORM:
                return uniform_mutation
            case constants.GAUSS:
                return gaussian_mutation
            case _:
                raise ValueError(f"Unknown selection method: {name}")

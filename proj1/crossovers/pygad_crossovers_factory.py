import benchmark_functions
import numpy as np

from proj1 import constants


def discrete_crossover(parents, offspring_size, ga_instance):
    num_parents, num_genes = parents.shape
    num_offspring = offspring_size[0]

    offspring = np.empty(offspring_size)

    for offspring_idx in range(ga_instance.sol_per_pop):
        parent1_idx = np.random.randint(0, num_parents)
        parent2_idx = np.random.randint(0, num_parents)

        for gene_idx in range(num_genes):
            if np.random.rand() < 0.5:
                offspring[offspring_idx, gene_idx] = parents[parent1_idx, gene_idx]
            else:
                offspring[offspring_idx, gene_idx] = parents[parent2_idx, gene_idx]

    return offspring

def arithmetic_crossover(parents, offspring_size, ga_instance):
    offspring = []
    idx = 0
    while len(offspring) < offspring_size[0]:
        parent1 = parents[idx % parents.shape[0], :].copy()
        parent2 = parents[(idx + 1) % parents.shape[0], :].copy()

        alpha = np.random.uniform(0, 1)
        child = alpha * parent1 + (1 - alpha) * parent2

        offspring.append(child)
        idx += 1

    return np.array(offspring)

def averaging_crossover(parents, offspring_size, ga_instance):
    offspring = []
    idx = 0
    while len(offspring) < offspring_size[0]:
        parent1 = parents[idx % parents.shape[0], :].copy()
        parent2 = parents[(idx + 1) % parents.shape[0], :].copy()

        child = (parent1 + parent2) / 2

        offspring.append(child)
        idx += 1

    return np.array(offspring)


class PygadCrossoverFactory:
    @staticmethod
    def get_crossover(name):
        match name:
            case constants.ONE_POINT:
                return "single_point"
            case constants.TWO_POINT:
                return "two_points"
            case constants.UNIFORM:
                return "uniform"
            case constants.DISCRETE:
                return discrete_crossover
            case constants.ARITHMETIC:
                return arithmetic_crossover
            case constants.AVERAGING:
                return averaging_crossover
            case _:
                raise ValueError(f"Unknown selection method: {name}")

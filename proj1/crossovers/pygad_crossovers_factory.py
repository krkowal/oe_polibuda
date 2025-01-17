import benchmark_functions
import numpy as np

from proj1 import constants


def discrete_crossover(parents, offspring_size, ga_instance):
    num_parents, num_genes = parents.shape
    num_offspring = offspring_size[0]

    offspring = np.empty(offspring_size)

    for offspring_idx in range(num_offspring):
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


def linear_crossover(parents, offspring_size, ga_instance):
    offspring = []
    idx = 0
    while len(offspring) < offspring_size[0]:
        parent1 = parents[idx % parents.shape[0], :].copy()
        parent2 = parents[(idx + 1) % parents.shape[0], :].copy()

        child1 = (parent1 + parent2) / 2
        child2 = 1.5 * parent1 - 0.5 * parent2
        child3 = -0.5 * parent1 + 1.5 * parent2

        offspring.extend([child1, child2, child3])
        if len(offspring) > offspring_size[0]:
            offspring = offspring[:offspring_size[0]]

        idx += 1

    return np.array(offspring)


def alpha_mixing_crossover(parents, offspring_size, ga_instance):
    offspring = []
    alpha = ga_instance.crossover_probability

    idx = 0
    while len(offspring) < offspring_size[0]:
        parent1 = parents[idx % parents.shape[0], :].copy()
        parent2 = parents[(idx + 1) % parents.shape[0], :].copy()

        child = alpha * parent1 + (1 - alpha) * parent2
        offspring.append(child)

        idx += 1

    return np.array(offspring)


def alpha_beta_mixing_crossover(parents, offspring_size, ga_instance):
    offspring = []
    idx = 0
    alpha = ga_instance.crossover_probability
    beta = 0.1

    while len(offspring) < offspring_size[0]:
        parent1 = parents[idx % parents.shape[0], :].copy()
        parent2 = parents[(idx + 1) % parents.shape[0], :].copy()

        child1_genes = alpha * parent1 + (1 - alpha) * parent2
        child2_genes = beta * parent1 + (1 - beta) * parent2

        offspring.append(child1_genes)
        if len(offspring) < offspring_size[0]:
            offspring.append(child2_genes)

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
            case constants.LINEAR:
                return linear_crossover
            case _:
                raise ValueError(f"Unknown selection method: {name}")

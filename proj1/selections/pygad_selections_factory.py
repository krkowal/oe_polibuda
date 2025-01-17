import benchmark_functions
import numpy as np

from proj1 import constants


def roulette_selection(fitness, num_parents, ga_instance):
    fitness = np.array(fitness)

    total_fitness = np.sum(fitness)
    if total_fitness == 0:
        raise ValueError("Total fitness is zero; cannot perform roulette selection.")
    selection_probabilities = fitness / total_fitness

    parents = np.empty((num_parents, ga_instance.population.shape[1]))
    selected_indices = []

    for _ in range(num_parents):
        selected_idx = np.random.choice(len(fitness), p=selection_probabilities)
        selected_indices.append(selected_idx)

        parents[len(selected_indices) - 1, :] = ga_instance.population[selected_idx, :].copy()

    return parents, np.array(selected_indices)


def tournament_selection(fitness, num_parents, ga_instance):
    tournament_size = ga_instance.K_tournament
    parents = np.empty((num_parents, ga_instance.population.shape[1]))
    selected_indices = []

    for parent_idx in range(num_parents):
        tournament_indices = np.random.choice(len(fitness), tournament_size, replace=False)
        tournament_fitness = [fitness[idx] for idx in tournament_indices]
        winner_idx = tournament_indices[np.argmin(tournament_fitness)]
        selected_indices.append(winner_idx)

        parents[parent_idx, :] = ga_instance.population[winner_idx, :].copy()

    return parents, np.array(selected_indices)


def best_selection(fitness, num_parents, ga_instance):
    fitness_sorted = sorted((range(len(fitness))), key=lambda k: fitness[k], reverse=False)
    parents = np.empty((num_parents, ga_instance.population.shape[1]))

    for parent_num in range(num_parents):
        parents[parent_num, :] = ga_instance.population[fitness_sorted[parent_num], :].copy()

    return parents, np.array(fitness_sorted[:num_parents])


class PygadSelectionFactory:
    @staticmethod
    def get_selection(name):
        match name:
            case constants.BEST:
                return best_selection
            case constants.ROULETTE:
                return roulette_selection
            case constants.TOURNAMENT:
                return tournament_selection
            case _:
                raise ValueError(f"Unknown selection method: {name}")

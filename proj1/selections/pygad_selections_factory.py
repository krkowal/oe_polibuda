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
    tournament_size = ga_instance.K_tournament  # Number of individuals in each tournament
    # print(tournament_size)
    parents = np.empty((num_parents, ga_instance.population.shape[1]))
    selected_indices = []

    for parent_idx in range(num_parents):
        tournament_indices = np.random.choice(len(fitness), tournament_size, replace=False)
        tournament_fitness = [fitness[idx] for idx in tournament_indices]
        print(tournament_indices)
        print(tournament_fitness)
        winner_idx = tournament_indices[np.argmin(tournament_fitness)]
        print(winner_idx)
        selected_indices.append(winner_idx)

        parents[parent_idx, :] = ga_instance.population[winner_idx, :].copy()

    return parents, np.array(selected_indices)


def best_selection(fitness, num_parents, ga_instance):
    # print(fitness)
    fitness_sorted = sorted((range(len(fitness))), key=lambda k: fitness[k], reverse=False)
    # print(fitness_sorted)
    parents = np.empty((num_parents, ga_instance.population.shape[1]))

    for parent_num in range(num_parents):
        parents[parent_num, :] = ga_instance.population[fitness_sorted[parent_num], :].copy()

    # print("pop")
    # print(ga_instance.population)
    # for i in ga_instance.population:
    #     print(i, benchmark_functions.StyblinskiTang(n_dimensions=ga_instance.num_genes)(i))
    # print("parents")
    # print(parents)
    # print("values")
    # print(np.array(fitness_sorted[:num_parents]))
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

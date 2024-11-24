import numpy as np

from constants import VALUE_FUNC_DIR
from proj1.Inversion import Inversion
from proj1.chromosomes.chromosome import Chromosome
from proj1.chromosomes.chromosome_list_factory import ChromosomeListFactory
from proj1.crossovers.crossover_factory import CrossoverFactory
from proj1.mutations.mutation_factory import MutationFactory
from proj1.selections.selection_factory import SelectionFactory


class Population:

    def __init__(self, chromosome_type, population_count: int, value_func_name: str, epochs: int, min_range: float,
                 max_range: float,
                 selection_name: str,
                 selection_param: int,
                 crossover_name: str, crossover_param: float, mutation_name: str, mutation_param: float,
                 inversion_param: float, genes_count: int,
                 has_elitism: bool = False,
                 elitism_count: int = 0,
                 is_maximization: bool = False):
        self._is_maximization = is_maximization
        self._epochs = epochs
        self._population_count = population_count
        self._value_func_name = value_func_name
        self._value_func = VALUE_FUNC_DIR[value_func_name]
        self._gens_count = genes_count
        self._min_range = min_range
        self._max_range = max_range
        # self._selection = Selection(selection_name, selection_param, has_elitism=has_elitism,
        #                             elitism_count=elitism_count, is_maximization=is_maximization)
        self._selection = SelectionFactory.get_selection(selection_name, selection_param, has_elitism=has_elitism,
                                                         elitism_count=elitism_count,
                                                         is_maximization=is_maximization)
        self._crossover = CrossoverFactory.get_crossover(crossover_name, population_count, crossover_param,
                                                         elite_count=elitism_count)
        self._mutation = MutationFactory.get_mutation(mutation_name, mutation_param)
        self._inversion = Inversion(inversion_param)
        self._has_elitism = has_elitism
        self._elitism_count = elitism_count
        # self._chromosomes_list = [
        #     BinaryChromosome(gens_count=self._gens_count, min_range=min_range, max_range=max_range) for
        #     _ in range(population_count)]
        self._chromosomes_list = ChromosomeListFactory.get_chromosome_list(chromosome_type,
                                                                           population_count=population_count,
                                                                           gens_count=genes_count,
                                                                           min_range=min_range, max_range=max_range)

    def evaluate_chromosomes(self) -> list[tuple[Chromosome, float]]:
        return list(zip(self._chromosomes_list,
                        list(map(lambda chromosome: chromosome.get_value(self._value_func), self._chromosomes_list))))

    def population_loop(self) -> tuple[list[list[float]], list[float], int | float]:
        all_values = []
        final_value = 0
        best_values = []
        for i in range(self._epochs):
            selected_chromosomes_list = self._selection.select(self.evaluate_chromosomes())
            elite_chromosomes_list = []
            if self._has_elitism:
                elite_chromosomes_list = [chromosome for chromosome, value in
                                          selected_chromosomes_list[:self._elitism_count]]
                selected_chromosomes_list = selected_chromosomes_list[self._elitism_count:]

            crossed_chromosome_list = self._crossover.cross(selected_chromosomes_list)
            crossed_chromosome_list = crossed_chromosome_list[:self._population_count - self._elitism_count]
            mutated_chromosomes_list = self._mutation.mutate(crossed_chromosome_list)

            inverted_chromosomes = self._inversion.invert(mutated_chromosomes_list)

            elite_chromosomes_list.extend(inverted_chromosomes)
            self._chromosomes_list = elite_chromosomes_list

            evaluation = self.evaluate_chromosomes()
            values = [value for _, value in evaluation]

            final_value = max(values) if self._is_maximization else min(values)
            best_values.append(max(values) if self._is_maximization else min(values))
            all_values.append(values)

            # print(f"Epoch {i + 1}/{self._epochs}")
            # print(values)
            # print(f"Worst value in this epoch: {min(values) if self._is_maximization else max(values)}")
            # print(f"Best value in this epoch: {max(values) if self._is_maximization else min(values) }")
            # print(f"Mean value in this epoch: {sum(values) / len(values)}")

        return all_values, best_values, final_value

import benchmark_functions
import numpy as np
import pygad

from constants import VALUE_FUNC_DIR, BINARY
from proj1.Inversion import Inversion
from proj1.chromosomes.chromosome import Chromosome
from proj1.chromosomes.chromosome_list_factory import ChromosomeListFactory
from proj1.crossovers.crossover_factory import CrossoverFactory
from proj1.crossovers.pygad_crossovers_factory import PygadCrossoverFactory
from proj1.mutations.mutation_factory import MutationFactory
from proj1.mutations.pygad_mutations_factory import PygadMutationFactory
from proj1.selections.pygad_selections_factory import PygadSelectionFactory
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
        self._selection_name = selection_name
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

            inverted_chromosomes = self._inversion.invert(
                mutated_chromosomes_list) if self._selection_name == BINARY else mutated_chromosomes_list

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

    def test_iteration(self):
        print("start")

        for chromosome, value in self.evaluate_chromosomes():
            print(chromosome.get_genes_list(), value)
        selected_chromosomes_list = self._selection.select(self.evaluate_chromosomes())
        elite_chromosomes_list = []
        if self._has_elitism:
            elite_chromosomes_list = [chromosome for chromosome, value in
                                      selected_chromosomes_list[:self._elitism_count]]
            selected_chromosomes_list = selected_chromosomes_list[self._elitism_count:]
        print("select")

        for chromosome, value in selected_chromosomes_list:
            print(chromosome.get_genes_list(), value)

        # print("mutate")
        # crossed_chromosome_list = self._crossover.cross(selected_chromosomes_list)
        # crossed_chromosome_list = crossed_chromosome_list[:self._population_count - self._elitism_count]

        # for chromosome, value in selected_chromosomes_list:
        #     print(chromosome.get_genes_list(), value)
        print("mutate")

        mutated_chromosomes_list = self._mutation.mutate([chromosome for chromosome, value in
                                                          selected_chromosomes_list])
        for chromosome in mutated_chromosomes_list:
            print(chromosome.get_genes_list())

    def pygad_iteration(self):

        is_minimum = True
        func = benchmark_functions.StyblinskiTang(n_dimensions=5)
        minimum = func.minimum().score
        is_minimum = True

        # print(minimum)

        def fitness_func(ga_instance, solution, solution_idx):
            # func.
            # print(solution)
            value = func(solution)
            # print(minimum)
            shifted_value = value + abs(minimum) + 1e-6
            # print(shifted_value)
            if is_minimum:
                return shifted_value
            return 1 / shifted_value

        def f(ga_instance, solution, solution_idx):
            return 1 / func(solution)

        num_generations = 100
        sol_per_pop = 80
        num_parents_mating = 50
        # boundary = func.suggested_bounds() #możemy wziąć stąd zakresy
        init_range_low = -32.768
        init_range_high = 32.768
        mutation_num_genes = 1
        parent_selection_type = "tournament"
        crossover_type = PygadCrossoverFactory.get_crossover("discrete")
        mutation_type = "random"

        selection = PygadSelectionFactory.get_selection("best")

        ga_instance = pygad.GA(num_generations=10,
                               sol_per_pop=10,
                               num_parents_mating=10,
                               fitness_func=fitness_func,
                               # gene_type=float,
                               num_genes=5,
                               parent_selection_type=selection,
                               mutation_num_genes=1,
                               init_range_low=-5,
                               init_range_high=5,
                               crossover_type=crossover_type,
                               crossover_probability=0.1,
                               # keep_elitism=1,
                               K_tournament=3,
                               parallel_processing=['thread', 4]
                               )

        ga_instance.run()

        best = ga_instance.best_solution()
        solution, solution_fitness, solution_idx = ga_instance.best_solution()

        print("Parameters of the best solution : {solution}".format(solution=solution))
        print(best)
        print(max(list(map(lambda x: func(x), ga_instance.population))))
        print(min(list(map(lambda x: func(x), ga_instance.population))))

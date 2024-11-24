import random

from proj1.selections.selection import Selection


class RouletteSelection(Selection):
    def __init__(self, param, has_elitism=False,
                 elitism_count=0, is_maximization=False):
        super().__init__(has_elitism, elitism_count, is_maximization)
        self._param = param

    def selection_function(self):
        fitness_values = [value for chromosome, value in self.current_chromosome_list] if self._is_maximization else [
            1 / value for chromosome, value in self.current_chromosome_list]
        total_fitness = sum(fitness_values)
        relative_fitness = [fitness / total_fitness for fitness in fitness_values]
        cumulative_probabilities = []
        cumulative_sum = 0
        for rf in relative_fitness:
            cumulative_sum += rf
            cumulative_probabilities.append(cumulative_sum)

        selected_chromosomes = set()
        while len(selected_chromosomes) < self._param - self._elitism_count:
            random_value = random.random()
            for i, cumulative_probability in enumerate(cumulative_probabilities):
                if random_value < cumulative_probability:
                    selected_chromosomes.add(self.current_chromosome_list[i])
                    break
        return selected_chromosomes

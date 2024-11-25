from abc import ABC
from typing import List
import random
from proj1.chromosomes.chromosome import Chromosome
from proj1.mutations.mutation import Mutation


class RealMutation(Mutation, ABC):

    def __init__(self, mutation_param):
        self._mutation_param = mutation_param

    def mutate(self, chromosomes_list) -> List[Chromosome]:
        new_chromosomes = []
        for chromosome in chromosomes_list:
            rand_value = random.random()
            if rand_value < self._mutation_param:
                new_chromosome = chromosome.from_crossover_and_mutations(chromosome, self.mutation_function(
                    chromosome))
                new_chromosomes.append(new_chromosome)
            else:
                new_chromosomes.append(chromosome)

        return new_chromosomes

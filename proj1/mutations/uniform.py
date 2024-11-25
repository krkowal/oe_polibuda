import random

from proj1.chromosomes.real import RealChromosome
from proj1.mutations.real_mutation import RealMutation


class UniformMutation(RealMutation):

    def __init__(self, mutation_param):
        super().__init__(mutation_param)

    def mutation_function(self, chromosome: RealChromosome):
        genotype = chromosome.get_genes_list()
        position: int = random.randrange(0, len(genotype), 1)
        genotype[position] = random.uniform(chromosome.min_range, chromosome.max_range)

        return genotype

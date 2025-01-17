import numpy as np
from proj1.chromosomes.real import RealChromosome
from proj1.crossovers.real_crossover import RealCrossover


class AlphaBetaMixingCrossover(RealCrossover):
    def __init__(self, population_count, crossover_param,crossover_param2, elite_count=0):
        super().__init__(population_count, elite_count)
        self._alpha = crossover_param
        self._beta = crossover_param2

    def _crossover_function(self, chromosome_list: list[RealChromosome]) -> list[RealChromosome]:
        parent1, parent2 = chromosome_list
        genes1 = parent1.get_genes_list()
        genes2 = parent2.get_genes_list()

        child1_genes = [
            self._alpha * g1 + (1 - self._alpha) * g2
            for g1, g2 in zip(genes1, genes2)
        ]
        child2_genes = [
            self._beta * g1 + (1 - self._beta) * g2
            for g1, g2 in zip(genes1, genes2)
        ]
        return [
            RealChromosome.from_crossover_and_mutations(parent1, child1_genes),
            RealChromosome.from_crossover_and_mutations(parent1, child2_genes),
        ]
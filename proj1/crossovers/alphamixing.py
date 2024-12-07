from proj1.chromosomes.real import RealChromosome
from proj1.crossovers.real_crossover import RealCrossover


class AlphaMixingCrossover(RealCrossover):
    def __init__(self, population_count, crossover_param, elite_count=0):
        super().__init__(population_count, elite_count)
        self._alpha = crossover_param

    def _crossover_function(self, chromosome_list: list[RealChromosome]) -> list[RealChromosome]:
        parent1, parent2 = chromosome_list
        genes1 = parent1.get_genes_list()
        genes2 = parent2.get_genes_list()

        child_genes = [
            self._alpha * g1 + (1 - self._alpha) * g2
            for g1, g2 in zip(genes1, genes2)
        ]
        return [RealChromosome.from_crossover_and_mutations(parent1, child_genes)]

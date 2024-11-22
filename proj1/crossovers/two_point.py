from proj1.Chromosome import Chromosome
from proj1.crossovers.n_point import NPointCrossover


class TwoPointCrossover(NPointCrossover):

    def __init__(self, population_count, crossover_param, elite_count=0):
        super().__init__(population_count, elite_count)
        self._crossover_param = crossover_param

    def _crossover_function(self, chromosome_list: list[Chromosome]) -> list[Chromosome]:
        return self.n_point_crossover(chromosome_list, 2)

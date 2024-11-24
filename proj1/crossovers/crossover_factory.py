from proj1.crossovers.crossover import Crossover
from proj1 import constants
from proj1.crossovers.discrete import DiscreteCrossover
from proj1.crossovers.one_point import OnePointCrossover
from proj1.crossovers.two_point import TwoPointCrossover
from proj1.crossovers.uniform import UniformCrossover


class CrossoverFactory:
    @staticmethod
    def get_crossover(name, population_count, crossover_param, elite_count) -> Crossover:
        match name:
            case constants.ONE_POINT:
                return OnePointCrossover(population_count, crossover_param, elite_count)
            case constants.TWO_POINT:
                return TwoPointCrossover(population_count, crossover_param, elite_count)
            case constants.UNIFORM:
                return UniformCrossover(population_count, crossover_param, elite_count)
            case constants.DISCRETE:
                return DiscreteCrossover(population_count, crossover_param, elite_count)
            case _:
                raise ValueError(f"Unknown crossover method: {name}")

from proj1.crossovers.crossover import Crossover
from proj1 import constants
from proj1.crossovers.discrete import DiscreteCrossover
from proj1.crossovers.one_point import OnePointCrossover
from proj1.crossovers.two_point import TwoPointCrossover
from proj1.crossovers.uniform import UniformCrossover
from proj1.crossovers.arithmetic import ArithmeticCrossover
from proj1.crossovers.linear import LinearCrossover
from proj1.crossovers.alphamixing import AlphaMixingCrossover
from proj1.crossovers.alphabetamixing import AlphaBetaMixingCrossover
from proj1.crossovers.averaging import AveragingCrossover



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
            case constants.ARITHMETIC:
                return ArithmeticCrossover(population_count, crossover_param, elite_count)
            case constants.LINEAR:
                return LinearCrossover(population_count, crossover_param, elite_count)
            case constants.ALPHA:
                return AlphaMixingCrossover(population_count, crossover_param, elite_count)
            case constants.ALPHABETA:
                return AlphaBetaMixingCrossover(population_count, crossover_param, elite_count)
            case constants.AVERAGING:
                return AveragingCrossover(population_count, crossover_param, elite_count)
            case _:
                raise ValueError(f"Unknown crossover method: {name}")

import benchmark_functions
import numpy as np

from proj1 import constants


def one_point_mutation(offspring, ga_instance):
    pass


class PygadMutationFactory:
    @staticmethod
    def get_mutation(name):
        match name:
            case constants.ONE_POINT:
                return OnePointMutation(mutation_param)
            case constants.TWO_POINT:
                return TwoPointMutation(mutation_param)
            case constants.BOUNDARY:
                return BoundaryMutation(mutation_param)
            case constants.UNIFORM:
                return UniformMutation(mutation_param)
            case constants.GAUSS:
                return GaussMutation(mutation_param)
            case _:
                raise ValueError(f"Unknown selection method: {name}")

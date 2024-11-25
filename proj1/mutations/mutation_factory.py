from proj1.mutations.boundary import BoundaryMutation
from proj1.mutations.gauss import GaussMutation
from proj1.mutations.mutation import Mutation
from proj1 import constants
from proj1.mutations.one_point import OnePointMutation
from proj1.mutations.two_point import TwoPointMutation
from proj1.mutations.uniform import UniformMutation


class MutationFactory:
    @staticmethod
    def get_mutation(name, mutation_param) -> Mutation:
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
                raise ValueError(f"Unknown mutation method: {name}")

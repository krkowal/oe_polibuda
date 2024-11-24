from proj1.mutations.boundary import BoundaryMutation
from proj1.mutations.mutation import Mutation
from proj1 import constants
from proj1.mutations.one_point import OnePointMutation
from proj1.mutations.two_point import TwoPointMutation


class MutationFactory:
    @staticmethod
    def get_mutation(name, muatation_param) -> Mutation:
        match name:
            case constants.ONE_POINT:
                return OnePointMutation(muatation_param)
            case constants.TWO_POINT:
                return TwoPointMutation(muatation_param)
            case constants.UNIFORM:
                return BoundaryMutation(muatation_param)
            case _:
                raise ValueError(f"Unknown mutation method: {name}")

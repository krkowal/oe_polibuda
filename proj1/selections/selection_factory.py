from proj1 import constants
from proj1.selections.best import BestSelection
from proj1.selections.roulette import RouletteSelection
from proj1.selections.selection import Selection
from proj1.selections.tournament import TournamentSelection


class MutationFactory:
    @staticmethod
    def get_mutation(name, has_elitism=False,
                     elitism_count=0, is_maximization=False) -> Selection:
        match name:
            case constants.BEST:
                return BestSelection(name, has_elitism, elitism_count, is_maximization)
            case constants.ROULETTE:
                return RouletteSelection(name, has_elitism, elitism_count, is_maximization)
            case constants.TOURNAMENT:
                return TournamentSelection(name, has_elitism, elitism_count, is_maximization)
            case _:
                raise ValueError(f"Unknown selection method: {name}")

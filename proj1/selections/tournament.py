import random

from proj1.selections.selection import Selection, get_sorted_chromosome_values


class TournamentSelection(Selection):

    def __init__(self, param, has_elitism=False,
                 elitism_count=0, is_maximization=False):
        super().__init__(has_elitism, elitism_count, is_maximization)
        self._param = param

    def selection_function(self):
        random.shuffle(self.current_chromosome_list)
        groups_list = [self.current_chromosome_list[i:i + self._param] for i in
                       range(0, len(self.current_chromosome_list), self._param)]

        winner_chromosome_list = [group[0] for group in
                                  [get_sorted_chromosome_values(shuffled_group, is_reversed=self._is_maximization) for
                                   shuffled_group in groups_list]]

        return winner_chromosome_list

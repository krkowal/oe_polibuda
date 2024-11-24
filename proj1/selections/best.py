from proj1.selections.selection import Selection, get_sorted_chromosome_values


class BestSelection(Selection):

    def __init__(self, param, has_elitism=False,
                 elitism_count=0, is_maximization=False):
        super().__init__(has_elitism, elitism_count, is_maximization)
        # self.__current_chromosome_list = None
        self._param = param

    def selection_function(self):
        sorted_chromosome_list = get_sorted_chromosome_values(self.current_chromosome_list,
                                                              is_reversed=self._is_maximization)
        return sorted_chromosome_list[:self._param - self._elitism_count]

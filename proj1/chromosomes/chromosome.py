from abc import ABC, abstractmethod


class Chromosome(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def get_value(self, func) -> float:
        pass

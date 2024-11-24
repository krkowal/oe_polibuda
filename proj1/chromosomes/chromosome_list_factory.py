from typing import List

from proj1.chromosomes.binary import BinaryChromosome
from proj1.chromosomes.chromosome import Chromosome
from proj1.chromosomes.real import RealChromosome
from proj1 import constants


class ChromosomeListFactory:
    @staticmethod
    def get_chromosome_list(name, population_count, gens_count, min_range, max_range) -> List[Chromosome]:
        match name:
            case constants.BINARY:
                return [BinaryChromosome(gens_count, min_range, max_range) for _ in range(population_count)]
            case constants.REAL:
                return [RealChromosome(gens_count, min_range, max_range) for _ in range(population_count)]
            case _:
                raise ValueError(f"Unknown chromosome list method: {name}")

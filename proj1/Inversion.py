import random

from proj1.chromosomes.binary import BinaryChromosome


class Inversion:
    def __init__(self, inversion_param):
        self._inversion_param = inversion_param

    def invert(self, chromosomes_list) -> list[BinaryChromosome]:
        new_chromosomes_list = []
        for chromosome in chromosomes_list:
            new_genes = []
            for gene in chromosome.get_genes_list():
                random_value = random.random()
                if random_value < self._inversion_param:
                    inversion_points = set()
                    while len(inversion_points) < 2:
                        inversion_points.add(random.randint(0, len(gene) - 1))
                    sorted_points = sorted(inversion_points)
                    new_genes.append(
                        gene[:sorted_points[0]] + gene[sorted_points[1]:sorted_points[0]:-1] + gene[sorted_points[1]:])
                else:
                    new_genes.append(gene)
            new_chromosomes_list.append(BinaryChromosome.from_crossover_and_mutations(chromosome, new_genes))
        return new_chromosomes_list

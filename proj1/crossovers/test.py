import unittest
from proj1.chromosomes.real import RealChromosome
from proj1.crossovers.arithmetic import ArithmeticCrossover
from proj1.crossovers.linear import LinearCrossover
from proj1.crossovers.alphamixing import AlphaMixingCrossover
from proj1.crossovers.alphabetamixing import AlphaBetaMixingCrossover
from proj1.crossovers.averaging import AveragingCrossover

class TestCrossovers(unittest.TestCase):
    def setUp(self):
        # Set up two parent chromosomes for testing
        self.parent1 = RealChromosome(3, 0, 10, genes=[1.0, 2.0, 3.0])
        self.parent2 = RealChromosome(3, 0, 10, genes=[4.0, 5.0, 6.0])
        self.chromosome_list = [self.parent1, self.parent2]

    def test_arithmetic_crossover(self):
        crossover = ArithmeticCrossover(population_count=10, crossover_param=0.5)
        offspring = crossover._crossover_function(self.chromosome_list)
        self.assertEqual(len(offspring), 1)
        child_genes = offspring[0].get_genes_list()
        for g1, g2, gc in zip(self.parent1.get_genes_list(), self.parent2.get_genes_list(), child_genes):
            self.assertAlmostEqual(gc, 0.5 * g1 + 0.5 * g2, delta=1e-6)

    def test_linear_crossover(self):
        crossover = LinearCrossover(population_count=10, crossover_param=0.5)
        offspring = crossover._crossover_function(self.chromosome_list)
        self.assertEqual(len(offspring), 3)
        child1_genes = offspring[0].get_genes_list()
        child2_genes = offspring[1].get_genes_list()
        child3_genes = offspring[2].get_genes_list()

        for g1, g2, c1, c2, c3 in zip(
            self.parent1.get_genes_list(),
            self.parent2.get_genes_list(),
            child1_genes,
            child2_genes,
            child3_genes,
        ):
            self.assertAlmostEqual(c1, (g1 + g2) / 2, delta=1e-6)
            self.assertAlmostEqual(c2, 1.5 * g1 - 0.5 * g2, delta=1e-6)
            self.assertAlmostEqual(c3, -0.5 * g1 + 1.5 * g2, delta=1e-6)

    def test_alpha_mixing_crossover(self):
        alpha = 0.7
        crossover = AlphaMixingCrossover(population_count=10, crossover_param=alpha)
        offspring = crossover._crossover_function(self.chromosome_list)
        self.assertEqual(len(offspring), 1)
        child_genes = offspring[0].get_genes_list()
        for g1, g2, gc in zip(self.parent1.get_genes_list(), self.parent2.get_genes_list(), child_genes):
            self.assertAlmostEqual(gc, alpha * g1 + (1 - alpha) * g2, delta=1e-6)

    def test_alpha_beta_mixing_crossover(self):
        alpha, beta = 0.6, 0.3
        crossover = AlphaBetaMixingCrossover(population_count=10, crossover_param=alpha)
        offspring = crossover._crossover_function(self.chromosome_list)
        self.assertEqual(len(offspring), 2)

        child1_genes = offspring[0].get_genes_list()
        child2_genes = offspring[1].get_genes_list()

        for g1, g2, c1, c2 in zip(
            self.parent1.get_genes_list(),
            self.parent2.get_genes_list(),
            child1_genes,
            child2_genes,
        ):
            self.assertAlmostEqual(c1, alpha * g1 + (1 - alpha) * g2, delta=1e-6)
            self.assertAlmostEqual(c2, beta * g1 + (1 - beta) * g2, delta=1e-6)

    def test_averaging_crossover(self):
        crossover = AveragingCrossover(population_count=10, crossover_param=0.6)
        offspring = crossover._crossover_function(self.chromosome_list)
        self.assertEqual(len(offspring), 1)
        child_genes = offspring[0].get_genes_list()
        for g1, g2, gc in zip(self.parent1.get_genes_list(), self.parent2.get_genes_list(), child_genes):
            self.assertAlmostEqual(gc, (g1 + g2) / 2, delta=1e-6)


if __name__ == "__main__":
    unittest.main()
from Population import Population
from proj1 import constants
from Plotter import Plotter

if __name__ == '__main__':
    pop = Population("binary", population_count=8, max_range=5, min_range=-5,
                     value_func_name=constants.STYBLISNKI_TANG_FUNCTION,
                     selection_name=constants.BEST,
                     selection_param=4, is_maximization=False, crossover_name=constants.ONE_POINT, crossover_param=0.5,
                     mutation_name=constants.TWO_POINT, mutation_param=0.1,  # Adjusted mutation parameter
                     inversion_param=1, has_elitism=True,
                     elitism_count=2, epochs=100, genes_count=2)

    all_values, best_values, final_value = pop.population_loop()
    print("Final Value:", final_value)

    plotter = Plotter(output_dir='output')
    plotter.save_best_values(best_values)
    plotter.save_all_values(all_values)
    plotter.save_mean_and_std(all_values)
    plotter.save_best_value_and_std(best_values, all_values)

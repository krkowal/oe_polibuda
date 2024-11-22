import matplotlib.pyplot as plt
import numpy as np
import os


class Plotter:
    def __init__(self, output_dir='plots'):
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def _subsample(self, data, max_points=1000):
        length = len(data)
        if length <= max_points:
            return data
        step = length // max_points
        return data[::step]

    def save_best_values(self, best_values, filename='best_values.png', max_points=1000):
        sampled_iterations = self._subsample(list(range(1, len(best_values) + 1)), max_points)
        sampled_best_values = self._subsample(best_values, max_points)

        plt.figure(figsize=(19.2, 10.8))  # Full HD size in inches
        plt.plot(sampled_iterations, sampled_best_values, label='Najlepsza wartość funkcji')
        plt.xlabel('Epoka')
        plt.ylabel('Wartość funkcji')
        plt.title('Najlepsze wartości funkcji od kolejnej iteracji')
        plt.legend()
        plt.grid(True)
        plt.savefig(os.path.join(self.output_dir, filename))
        plt.close()

    def save_all_values(self, all_values, filename='all_values.png', max_points=1000):
        plt.figure(figsize=(19.2, 10.8))  # Full HD size in inches
        num_epochs = len(all_values)
        num_chromosomes = len(all_values[0])

        for i in range(num_chromosomes):
            chromosome_values = [epoch_values[i] for epoch_values in all_values]
            sampled_iterations = self._subsample(list(range(num_epochs)), max_points)
            sampled_values = self._subsample(chromosome_values, max_points)
            plt.plot(sampled_iterations, sampled_values, label=f'Chromosome {i + 1}')

        plt.xlabel('Epoka')
        plt.ylabel('Wartość funkcji')
        plt.title('Wszystkie wartości funkcji od kolejnej iteracji')
        plt.legend(loc='upper right')
        plt.grid(True)
        plt.savefig(os.path.join(self.output_dir, filename))
        plt.close()

    def save_mean_and_std(self, all_values, filename='mean_std.png', max_points=1000):
        means = []
        stds = []
        for values in all_values:
            means.append(np.mean(values))
            stds.append(np.std(values))

        iterations = list(range(1, len(means) + 1))
        sampled_iterations = self._subsample(iterations, max_points)
        sampled_means = self._subsample(means, max_points)
        sampled_stds = self._subsample(stds, max_points)

        plt.figure(figsize=(19.2, 10.8))  # Full HD size in inches
        plt.plot(sampled_iterations, sampled_means, label='Średnia wartość funkcji', color='blue')
        plt.fill_between(sampled_iterations, np.array(sampled_means) - np.array(sampled_stds),
                         np.array(sampled_means) + np.array(sampled_stds), color='blue', alpha=0.2, label='Odchylenie standardowe')
        plt.xlabel('Epoka')
        plt.ylabel('Wartość funkcji')
        plt.title('Średniej wartości funkcji, odchylenie standardowe od kolejnej iteracji')
        plt.legend()
        plt.grid(True)
        plt.savefig(os.path.join(self.output_dir, filename))
        plt.close()

    def save_best_value_and_std(self, best_values, all_values, filename='best_value_std.png', max_points=1000):
        best_stds = []
        for i, best_value in enumerate(best_values):
            epoch_values = np.array(all_values[i])
            best_stds.append(np.std(epoch_values[epoch_values >= best_value]))

        iterations = list(range(1, len(best_values) + 1))
        sampled_iterations = self._subsample(iterations, max_points)
        sampled_best_values = self._subsample(best_values, max_points)
        sampled_best_stds = self._subsample(best_stds, max_points)

        plt.figure(figsize=(19.2, 10.8))  # Full HD size in inches
        plt.plot(sampled_iterations, sampled_best_values, label='Najlepsza wartość funkcji', color='green')
        plt.fill_between(sampled_iterations, np.array(sampled_best_values) - np.array(sampled_best_stds),
                         np.array(sampled_best_values) + np.array(sampled_best_stds), color='green', alpha=0.2,
                         label='Odchylenie standardowe')
        plt.xlabel('Epoka')
        plt.ylabel('Wartość funkcji')
        plt.title('Najlepszej wartości funkcji, odchylenie standardowe od kolejnej iteracji')
        plt.legend()
        plt.grid(True)
        plt.savefig(os.path.join(self.output_dir, filename))
        plt.close()
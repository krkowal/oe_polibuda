import tkinter as tk
from tkinter import messagebox, ttk
import sys
from tkinter import messagebox
from proj1 import constants
try:
    from Population import Population
except ImportError:
    import sys
    sys.path.append(sys.path[0] + '/..')
    from Population import Population
try:
    from Plotter import Plotter
except ImportError:
    import sys
    sys.path.append(sys.path[0] + '/..')
    from Plotter import Plotter
sys.path.append('../Database')
try:
    from CSVFileWrite import CSVDataSaver
except ImportError:
    import sys
    sys.path.append(sys.path[0] + '/..')
    from Database.CSVFileWrite import CSVDataSaver
try:
    from DBconnect import connect_and_insert
except ImportError:
    import sys
    sys.path.append(sys.path[0] + '/..')
    from Database.DBconnect import connect_and_insert







sys.path.append("proj1")
import numpy as np


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Genetic Algorithm")
        self.geometry("400x800")

        self.elapsed_time = 0
        self.timer_running = False
        self.timer_job = None

        self.placeholders = [
            'Population amount', 'Begin of the range - a', 'End of the range - b',
            'Selection parameter', 'Crossover probability', 'Mutation probability',
            'Inversion probability', 'Elite Strategy amount', 'Epochs amount', 'Genes count'
        ]
        self.create_widgets()

    def create_widgets(self):
        self.timer_label = tk.Label(self, text="Elapsed Time: 0s", font=("Arial", 12))
        self.timer_label.pack(pady=10)

        self.textboxes = []
        for placeholder in self.placeholders:
            textbox = tk.Entry(self)
            textbox.pack(pady=5, fill=tk.X, padx=10)
            self.set_placeholder(textbox, placeholder)
            self.textboxes.append(textbox)

        self.combo_labels_text = [
            "Choose selection method",
            "Choose crossover method",
            "Choose mutation method",
            "Choose function"
        ]

        self.combobox_values = [
            [constants.BEST, constants.ROULETTE, constants.TOURNAMENT],
            [constants.ONE_POINT, constants.TWO_POINT, constants.UNIFORM, constants.DISCRETE],
            [constants.ONE_POINT, constants.TWO_POINT],
            list(constants.VALUE_FUNC_DIR.keys())
        ]

        default_values = [constants.BEST, constants.ONE_POINT, constants.ONE_POINT, constants.PLAIN_FUNCTION]

        self.comboboxes = []
        for label_text, values, default in zip(self.combo_labels_text, self.combobox_values, default_values):
            label = tk.Label(self, text=label_text)
            label.pack(pady=5)
            combobox = ttk.Combobox(self, values=values, state="readonly")
            combobox.set(default)
            combobox.pack(pady=5, fill=tk.X, padx=10)
            self.comboboxes.append(combobox)

        self.checkbox_var = tk.BooleanVar()
        self.checkbox = tk.Checkbutton(self, text="Maximization", variable=self.checkbox_var)
        self.checkbox.pack(pady=5)

        self.checkbox_var2 = tk.BooleanVar()
        self.elitism_checkbox = tk.Checkbutton(self, text="Elitism", variable=self.checkbox_var2)
        self.elitism_checkbox.pack(pady=5)

        start_button = tk.Button(self, text="Start", command=self.start_timer)
        start_button.pack(pady=10, fill=tk.X, padx=10)

    def set_placeholder(self, widget, placeholder):
        widget.insert(0, placeholder)
        widget.bind("<FocusIn>", lambda event: self.clear_placeholder(event, placeholder))
        widget.bind("<FocusOut>", lambda event: self.add_placeholder(event, placeholder))

    def clear_placeholder(self, event, placeholder):
        if event.widget.get() == placeholder:
            event.widget.delete(0, tk.END)

    def add_placeholder(self, event, placeholder):
        if not event.widget.get():
            event.widget.insert(0, placeholder)

    def start_timer(self):
        if not self.timer_running:
            self.elapsed_time = 0
            self.timer_running = True
            self.update_timer()

        self.on_button_click()

    def stop_timer(self):
        if self.timer_running:
            self.timer_running = False
            if self.timer_job:
                self.after_cancel(self.timer_job)

    def update_timer(self):
        if self.timer_running:
            self.elapsed_time += 0.001
            self.timer_label.config(text=f"Elapsed Time: {self.elapsed_time}s")

            self.timer_job = self.after(1, self.update_timer)

    def on_button_click(self):
        textbox_values = [textbox.get() for textbox in self.textboxes]
        combobox_values = [combobox.get() for combobox in self.comboboxes]
        checkbox_value = self.checkbox_var.get()
        checkbox_value2 = self.checkbox_var2.get()


        selection_method = combobox_values[0]
        crossover_method = combobox_values[1]
        mutation_method = combobox_values[2]
        selected_function_key = combobox_values[3]

        pop = Population(
            population_count=int(textbox_values[0]),
            max_range=int(textbox_values[2]),
            min_range=int(textbox_values[1]),
            value_func_name=selected_function_key,
            selection_name=selection_method,
            selection_param=int(textbox_values[3]),
            is_maximization=checkbox_value,
            crossover_name=crossover_method,
            crossover_param=float(textbox_values[4]),
            mutation_name=mutation_method,
            mutation_param=float(textbox_values[5]),
            inversion_param=float(textbox_values[6]),
            has_elitism=checkbox_value2,
            elitism_count=int(textbox_values[7]),
            epochs=int(textbox_values[8]),
            genes_count=int(textbox_values[9])
        )

        all_values, best_values, final_value = pop.population_loop()
        self.stop_timer()
        print("Final Value:", final_value)
        data = [final_value]
        test = CSVDataSaver(data)
        test.save_to_csv()
        connect_and_insert(final_value)
        messagebox.showinfo("Final Value", "Final Value: " + str(final_value))

        plotter = Plotter(output_dir='output')
        plotter.save_best_values(best_values)
        plotter.save_all_values(all_values)
        plotter.save_mean_and_std(all_values)
        plotter.save_best_value_and_std(best_values, all_values)



if __name__ == "__main__":
    app = App()
    app.mainloop()


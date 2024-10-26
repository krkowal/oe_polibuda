import tkinter as tk
from tkinter import messagebox, ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Genetic Algorithm with Timer")
        self.geometry("300x700")

        # Initialize timer variables
        self.elapsed_time = 0
        self.timer_running = False
        self.timer_job = None

        self.placeholders = [
            'Begin of the range - a', 'End of the range - b', 'Population amount',
            'Number of bits', 'Epochs amount', 'Best and tournament chromosome amount',
            'Elite Strategy amount', 'Cross probability', 'Mutation probability', 'Inversion probability'
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
            "Choose cross method",
            "Choose mutation method"
        ]
        self.combobox_values = [
            ["BEST", "ROULETTE", "TOURNAMENT"],
            ["ONE_POINT", "TWO_POINT", "THREE_POINTS", "HOMO"],
            ["ONE_POINT", "TWO_POINT"]
        ]
        default_values = ["BEST", "ONE_POINT", "ONE_POINT"]

        self.comboboxes = []
        for label_text, values, default in zip(self.combo_labels_text, self.combobox_values, default_values):
            label = tk.Label(self, text=label_text)
            label.pack(pady=5)
            combobox = ttk.Combobox(self, values=values, state="readonly")
            combobox.set(default)
            combobox.pack(pady=5, fill=tk.X, padx=10)
            self.comboboxes.append(combobox)

        self.checkbox_var = tk.BooleanVar()
        self.checkbox = tk.Checkbutton(self, text="Check me", variable=self.checkbox_var)
        self.checkbox.pack(pady=5)

        self.function_var = tk.StringVar(value="Function1")  # Default to "Function1"
        function1_radio = tk.Radiobutton(self, text="Function1", variable=self.function_var, value="Function1")
        function2_radio = tk.Radiobutton(self, text="Function2", variable=self.function_var, value="Function2")
        function1_radio.pack(pady=5)
        function2_radio.pack(pady=5)

        start_button = tk.Button(self, text="Start", command=self.start_timer)
        start_button.pack(pady=10, fill=tk.X, padx=10)

        stop_button = tk.Button(self, text="Stop", command=self.stop_timer)
        stop_button.pack(pady=10, fill=tk.X, padx=10)

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
            self.elapsed_time += 1
            self.timer_label.config(text=f"Elapsed Time: {self.elapsed_time}s")

            self.timer_job = self.after(1000, self.update_timer)

    def on_button_click(self):
        textbox_values = [textbox.get() for textbox in self.textboxes]
        combobox_values = [combobox.get() for combobox in self.comboboxes]
        checkbox_value = self.checkbox_var.get()
        selected_function = self.function_var.get()


        messagebox.showinfo("Collected Data", f"Textbox Values: {textbox_values}\n"
                                              f"Combobox Values: {combobox_values}\n"
                                              f"Checkbox Value: {checkbox_value}")

if __name__ == "__main__":
    app = App()
    app.mainloop()
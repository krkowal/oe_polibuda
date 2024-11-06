import csv
import sys
import os
from datetime import datetime


class CSVDataSaver:
    def __init__(self, data):
        self.data = data

    def save_to_csv(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        directory = os.path.join(sys.path[0], "..", "Results")
        os.makedirs(directory, exist_ok=True)
        filename = os.path.join(directory, f"data_{timestamp}.csv")

        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for item in self.data:
                writer.writerow([item])

        print(f"Data saved to {filename}")

import csv
from datetime import datetime


class CSVDataSaver:
    def __init__(self, data):
        self.data = data

    def save_to_csv(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"data_{timestamp}.csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.data)
        print(f"Data saved to {filename}")

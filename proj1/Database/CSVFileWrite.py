import csv
import sys
from datetime import datetime


class CSVDataSaver:
    def __init__(self, data):
        self.data = data
        self.header = ["Final Value"]

    def save_to_csv(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = sys.path[0] + f"\..\Results\data_{timestamp}.csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.header)
            writer.writerow(self.data)
        print(f"Data saved to {filename}")

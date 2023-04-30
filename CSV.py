import pandas as pd


class CSV:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = pd.read_csv(self.file_path)

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

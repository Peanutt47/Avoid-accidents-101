import pandas as pd


class CSV:
    def __init__(self):
        self.data = pd.read_csv('accident2022.csv')

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

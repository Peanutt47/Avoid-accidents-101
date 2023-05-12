import pandas as pd


class CSV:
    def __init__(self, file_path):
        self.file_path = file_path
        try:
            self.data = pd.read_csv(self.file_path)
        except FileNotFoundError:
            self.data = False
        except Exception as e:
            print(e)
            self.data = False

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def check_file(self):
        return type(self.data) == pd.DataFrame

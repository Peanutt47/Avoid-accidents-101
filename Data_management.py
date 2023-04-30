import matplotlib as plt
import numpy as np
import pandas as pd
class Data_managemnt():
    def __init__(self, data):
        self.data = data

    def show(self):
        return self.data

    def histogram(self):
        plt.hist(self.data)
        plt.show()
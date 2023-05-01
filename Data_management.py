import matplotlib.pyplot as plt
import numpy as np


class Data_management():
    def __init__(self, data):
        self.data = data

    def show(self):
        return self.data

    def province_bar(self):
        plt.subplots(figsize=(13, 8))
        graph = plt.bar(self.data.จังหวัด.value_counts().index, self.data.จังหวัด.value_counts().values, color='green')
        graph.bar_label(graph, labels=self.data.จังหวัด.value_counts().values, rotation=45)
        graph.xticks(rotation=90, ha="right")
        accident_province_canvas = plt.FigureCanvasTkAgg(graph, self)
        return accident_province_canvas.get_tk_widget()

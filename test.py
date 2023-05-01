import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("accident2022(eng).csv")
plt.subplots(figsize=(13, 8))
x = plt.bar(df.จังหวัด.value_counts().index, df.จังหวัด.value_counts().values, color='green')
x.bar_label(x, labels=df.จังหวัด.value_counts().values, padding=3, rotation=45, fontsize=8)
x.xticks(rotation=90, ha='right')
x.show()
print(df.จังหวัด.value_counts())

# import tkinter as tk
# import matplotlib
#
# matplotlib.use('TkAgg')
#
# from matplotlib.figure import Figure
# from matplotlib.backends.backend_tkagg import (
#     FigureCanvasTkAgg,
#     NavigationToolbar2Tk
# )
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#
#         self.title('Tkinter Matplotlib Demo')
#
#         # prepare data
#         data = {
#             'Python': 11.27,
#             'C': 11.16,
#             'Java': 10.46,
#             'C++': 7.5,
#             'C#': 5.26
#         }
#         languages = data.keys()
#         popularity = data.values()
#
#         # create a figure
#         figure = Figure(figsize=(6, 4), dpi=100)
#         # create axes
#         axes = figure.add_subplot()
#
#         # create the barchart
#         axes.bar(languages, popularity)
#         axes.set_title('Top 5 Programming Languages')
#         axes.set_ylabel('Popularity')
#
#         # create FigureCanvasTkAgg object
#         figure_canvas = FigureCanvasTkAgg(figure, self)
#
#         # create the toolbar
#         NavigationToolbar2Tk(figure_canvas, self)
#
#         figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
#
#
# if __name__ == '__main__':
#     app = App()
#     app.mainloop()
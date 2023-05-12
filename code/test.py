import json
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from mpl_toolkits.basemap import Basemap

def create_basemap_plot(source_province=None, destination_province=None):
    # Your code for creating the Basemap plot goes here

    # Create a Figure and Axes object
    fig = plt.figure(figsize=(8, 6), dpi=100)
    ax = fig.add_subplot(111)

    # Draw the Basemap plot on the Axes object
    map = Basemap(llcrnrlon=98, llcrnrlat=6, urcrnrlon=105, urcrnrlat=20, resolution='l', ax=ax)
    map.drawcoastlines()
    map.drawcountries()

    # Plot nodes and edges on the map

    # Show the plot
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Add a toolbar
    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()
    canvas.get_tk_widget().pack()

    # Return the Figure object
    return fig

# Create a Tkinter window
window = tk.Tk()

# Call the create_basemap_plot function
fig = create_basemap_plot(source_province='Bangkok', destination_province='Chiang Mai')

# Start the Tkinter event loop
window.mainloop()

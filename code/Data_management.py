import json

import networkx as nx
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np


class Data_management():
    def __init__(self, data):
        self.data = data

    def show(self):
        return self.data

    def province_bar(self):
        fig = plt.Figure(figsize=(12, 6), dpi=100)
        ax_bar = fig.add_subplot()
        ax_bar.bar(self.data.จังหวัด.value_counts().index, self.data.จังหวัด.value_counts().values, color='green')
        ax_bar.bar_label(ax_bar.containers[0], labels=self.data.จังหวัด.value_counts().values, rotation=30, fontsize=7)
        tick_labels = self.data.จังหวัด.value_counts().index
        tick_positions = range(len(tick_labels))
        ax_bar.set_xticks(tick_positions)
        ax_bar.set_xticklabels(tick_labels, rotation=45, ha="right", fontsize=7)
        ax_bar.set_xlabel("province")
        ax_bar.set_ylabel("accident")
        ax_bar.set_title("Accident per province")
        fig.tight_layout()
        return fig
        # graph = plt.bar(self.data.จังหวัด.value_counts().index, self.data.จังหวัด.value_counts().values, color='green')
        # graph.bar_label(graph, labels=self.data.จังหวัด.value_counts().values, rotation=45)
        # graph.xticks(rotation=90, ha="right")
        # accident_province_canvas = plt.FigureCanvasTkAgg(graph, self)
        # return accident_province_canvas.get_tk_widget()

    import json
    import tkinter as tk
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    from mpl_toolkits.basemap import Basemap
    import networkx as nx
    def get_province(self):
        with open('province.json', 'r') as file:
            data = json.load(file)
            return data
    def create_basemap_plot(self, source_province=None, destination_province=None):
        # Read data from files
        with open("thailand_province_relations.txt", "r") as file:
            data = file.read().splitlines()

        listf = []
        for i in data:
            source, destinations = i.split(" -> ")
            destinations_list = destinations.split(", ")
            for j in destinations_list:
                listf.append((source, j))

        with open('province.json', 'r') as file:
            data = json.load(file)

        # Create a Basemap object for Thailand
        fig = plt.figure(figsize=(8, 6), dpi=100)
        map = Basemap(llcrnrlon=97, llcrnrlat=5, urcrnrlon=106, urcrnrlat=21, resolution='l')

        # Draw coastlines and country borders
        map.drawcoastlines()
        map.drawcountries()

        # Create a graph using NetworkX
        G = nx.Graph()

        # Add nodes to the graph
        for province, coordinates in data.items():
            lat, lon = coordinates
            x, y = map(lon, lat)
            G.add_node(province, pos=(x, y))

        # Add edges to the graph
        for edge in listf:
            source, destination = edge
            source_coords = data[source]
            destination_coords = data[destination]
            lat1, lon1 = source_coords
            lat2, lon2 = destination_coords
            x1, y1 = map(lon1, lat1)
            x2, y2 = map(lon2, lat2)
            G.add_edge(source, destination, weight=((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)

        if source_province and destination_province:
            # Find the shortest path
            shortest_path = nx.dijkstra_path(G, source_province, destination_province)

        # Plot the nodes on the map
        for province, coordinates in data.items():
            lat, lon = coordinates
            x, y = map(lon, lat)
            if source_province and destination_province and province in shortest_path:
                map.plot(x, y, 'ro', markersize=6)  # Red circles for the shortest path nodes
            else:
                map.plot(x, y, 'bo', markersize=6)  # Blue circles for other nodes
            plt.text(x, y, province, fontsize=8, ha='center', va='bottom')

        # Plot the edges on the map
        for edge in listf:
            source, destination = edge
            source_coords = data[source]
            destination_coords = data[destination]
            lat1, lon1 = source_coords
            lat2, lon2 = destination_coords
            x1, y1 = map(lon1, lat1)
            x2, y2 = map(lon2, lat2)
            if source_province and destination_province and source in shortest_path and destination in shortest_path:
                map.plot([x1, x2], [y1, y2], 'r', alpha=0.6)  # Red lines for the shortest path edges
            else:
                map.plot([x1, x2], [y1, y2], 'gray', alpha=0.6)

        # Show the map
        plt.title("Province Connections")

        return fig

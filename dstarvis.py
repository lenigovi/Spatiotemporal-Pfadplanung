import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import matplotlib.animation as animation

# Dijkstra's algorithm implementation
def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    nodes = list(graph)
    path = []

    while nodes:
        current_node = min(nodes, key=lambda node: distances[node])
        nodes.remove(current_node)
        
        if distances[current_node] == float('infinity'):
            break
        
        for neighbor, cost in graph[current_node].items():
            alternative_route = distances[current_node] + cost
            if alternative_route < distances[neighbor]:
                distances[neighbor] = alternative_route
                previous_nodes[neighbor] = current_node
                path.append((current_node, neighbor))
    
    return previous_nodes, distances, path

# Graph definition

graph = {
    'A': {'B': 5, 'C': 3, 'D': 6},
    'B': {'C': 6, 'E': 4},
    'C': {'D': 7, 'E': 6},
    'D': {'E': 2, 'F': 2},
    'E': {'G': 3},
    'F': {'G': 5},
    'G': {}
}

# Redefine the Dijkstra function to handle graphs without certain edges
def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    nodes = list(graph)
    path = []

    while nodes:
        current_node = min(nodes, key=lambda node: distances[node])
        nodes.remove(current_node)
        
        if distances[current_node] == float('infinity'):
            break
        
        for neighbor, cost in graph[current_node].items():
            alternative_route = distances[current_node] + cost
            if alternative_route < distances[neighbor]:
                distances[neighbor] = alternative_route
                previous_nodes[neighbor] = current_node
                path.append((current_node, neighbor))
    
    return previous_nodes, distances, path

# Run Dijkstra's algorithm again with the corrected graph
start_node = 'A'
previous_nodes, distances, path = dijkstra(graph, start_node)

# Create the graph
G = nx.DiGraph()
for node, edges in graph.items():
    for edge, weight in edges.items():
        G.add_edge(node, edge, weight=weight)

# Position the nodes based on a fixed layout similar to the image
pos = {
    'A': (0, 0),
    'B': (0, 1),
    'C': (1, 0.5),
    'D': (2, 0),
    'E': (2, 1),
    'F': (3, 0),
    'G': (3, 1)
}

# Draw the initial graph
fig, ax = plt.subplots()
nx.draw(G, pos, with_labels=True, node_color='lightgreen', ax=ax, node_size=2000, font_size=16, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax, font_size=16, font_color='black', bbox=dict(facecolor='white', edgecolor='none'))

# Function to update the graph
def update(num):
    ax.clear()
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', ax=ax, node_size=2000, font_size=16, font_weight='bold')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax, font_size=16, font_color='black', bbox=dict(facecolor='white', edgecolor='none'))
    if num < len(path):
        edge = path[num]
        nx.draw_networkx_edges(G, pos, edgelist=[edge], width=2.5, alpha=0.6, edge_color='red', ax=ax)

# Create animation
ani = animation.FuncAnimation(fig, update, frames=len(path), repeat=False)
plt.show()

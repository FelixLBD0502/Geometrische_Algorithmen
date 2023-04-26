from shapely.geometry import LineString, Point
import networkx as nx
import matplotlib.pyplot as plt

# Erstelle Linestrings
lines = [
    LineString([(0, 0), (1, 0)]),
    LineString([(0, 0), (0, 1)]),
    LineString([(1, 0), (2, 0)]),
    LineString([(0, 1), (1, 1)]),
    LineString([(1, 1), (2, 1)]),
    LineString([(2, 0), (3, 0)]),
    LineString([(2, 1), (3, 1)]),
    LineString([(3, 0), (4, 0)]),
    LineString([(3, 1), (4, 1)]),
    LineString([(1, 0), (1, 1)]),
    LineString([(2, 0), (2, 1)]),
    LineString([(3, 0), (3, 1)])
]

# Finde die Schnittpunkte der Linestrings
points = []
for i in range(len(lines)):
    for j in range(i+1, len(lines)):
        if lines[i].intersects(lines[j]):
            point = lines[i].intersection(lines[j])
            if isinstance(point, Point):
                points.append(point)

# Erstelle ein Graph-Objekt
G = nx.Graph()

# Füge die Knoten hinzu
for i, point in enumerate(points):
    G.add_node(i+1, pos=point.coords[0])

# Füge die Kanten hinzu
for i, line in enumerate(lines):
    for j, point in enumerate(points):
        if point == line.coords[0] or point == line.coords[-1]:
            G.add_edge(j+1, j+2)

# Entferne Knoten ohne Position
for node in list(G.nodes):
    if 'pos' not in G.nodes[node]:
        G.remove_node(node)

# Zeige den Graphen mit matplotlib an und speichere ihn als PDF-Datei
pos = nx.get_node_attributes(G, 'pos')
nx.draw(G, pos)
nx.draw_networkx_edges(G, pos, edgelist=[(i+1, j+1) for i in range(len(points)) for j in range(i+1, len(points))], edge_color='red')
plt.savefig("geo_netz.pdf")
plt.show()
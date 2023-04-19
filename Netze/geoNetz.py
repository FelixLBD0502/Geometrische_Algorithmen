import networkx as nx
import matplotlib.pyplot as plt

# Erstelle ein Graph
G = nx.Graph()

# Füge die vier Knoten hinzu
G.add_node(1, pos=(0, 0))
G.add_node(2, pos=(0, 1))
G.add_node(3, pos=(1, 0))
G.add_node(4, pos=(1, 1))

# Füge die Kanten hinzu
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(1, 4)
G.add_edge(2, 3)
G.add_edge(2, 4)
G.add_edge(3, 4)

# Graphen mit matplotlib anzeigen und als PDF ausgeben
pos = nx.get_node_attributes(G, 'pos')
nx.draw(G, pos)
plt.savefig("geometrisches_netzwerk.pdf")


import networkx as nx

def create_graph():
    G = nx.Graph()

    G.add_weighted_edges_from([
        ("Entrance", "Hall", 5),
        ("Hall", "Kitchen", 3),
        ("Hall", "Bedroom", 4)
    ])

    return G
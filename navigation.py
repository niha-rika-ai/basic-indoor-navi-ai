import networkx as nx

def find_path(graph, start, end):
    return nx.shortest_path(graph, start, end, weight='weight')

directions = {
    ("Entrance", "Hall"): "Go straight",
    ("Hall", "Kitchen"): "Turn right",
    ("Hall", "Bedroom"): "Turn left"
}

def get_steps(path):
    steps = []
    for i in range(len(path)-1):
        step = directions.get((path[i], path[i+1]), "Move forward")
        steps.append(step)
    return steps
class Edge:
    def __init__(self, start, end, cost) -> None:
        #pass
        self.start = start
        self.end = end
        self.cost = cost

class Graph:
    def __init__(self, edges) -> None:
        self.edges = [create_node(*e) for e in edges]

    def vertices(self):
        return set(e.start for e in self.edges) \
        .union(e.end for e in self.edges)

    def get_neighbours(self, v):
        neighbours = []
        for e in self.edges:
            if e.start == v:
                neighbours.append((e.end, e.cost))
        return neighbours

    def dijkstra(self, source, dest):
        distances = {v: float("inf") for v in self.vertices()}
        prev_v = {v: None for v in self.vertices()}

        distances[source] = 0 # set start to cost 0
        vertices_copy = list(self.vertices())[:]

        while len(vertices_copy) > 0:
            v = min(vertices_copy, key=lambda u: distances[u]) # current node
            vertices_copy.remove(v)
            if (distances[v] == float("inf")):
                break

            for neighbour, cost in self.get_neighbours(v):
                path_cost = distances[v] + cost
                if path_cost < distances[neighbour]:
                    distances[neighbour] = path_cost
                    prev_v[neighbour] = v

        path = []
        curr_v = dest
        while prev_v[curr_v] is not None:
            path.insert(0, curr_v)
            curr_v = prev_v[curr_v]
        
        path.insert(0, curr_v)
        return path

def create_node(start, end, cost) -> Edge:
    return Edge(start, end, cost)

if __name__ == "__main__":
    graph = Graph([
        ("a", "b", 2), ("a", "c", 4), ("b", "c", 5), 
        ("b", "d", 4), ("b", "e", 9), ("c", "e", 1), 
        ("d", "e", 2), ("c", "g", 2), ("c", "h", 7), 
        ("g", "h", 3), ("g", "f", 1), ("h", "j", 5), 
        ("g", "j", 8), ("f", "i", 2), ("i", "j", 6), 
        ("g", "i", 6)
    ])

    print(graph.dijkstra("a", "i"))
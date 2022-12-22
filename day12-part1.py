import time
import heapq

CONST_START = "S"
CONST_END = "E"

class color:
   CYAN = '\033[96m'
   BOLD = '\033[1m'
   END = '\033[0m'

class Edge:
    def __init__(self, start, end, cost) -> None:
        self.start = start
        self.end = end
        self.cost = cost

class Vertex:
    def __init__(self, v_id, text, x, y, graph) -> None:
        self.v_id = v_id
        self.is_start = True if text == CONST_START else False
        self.is_end = True if text == CONST_END else False
        if self.is_start:
            text = "a"
        elif self.is_end:
            text = "z"

        self.text = text
        self.x = x
        self.y = y
        self.graph = graph
        self.cost_to_start = float("inf")
        self.neighbours = []

    def __str__(self) -> str:
        return self.text

    def __repr__(self) -> str:
        return self.text + " (" + str(self.x) + ", " + str(self.y) + ")"

    def __lt__(self, other):
        return self.cost_to_start < other.cost_to_start

    def get_neighbours(self):
        return self.neighbours

    def compute_neighbours(self):
        cost = 1

        if self.x > 0:
            n = self.graph.matrix[self.y][self.x - 1]
            if self.is_neighbour(n) and self.is_step_allowed(n):
                self.neighbours.append((n, cost))

        if self.x < len(self.graph.matrix[self.y]) - 1:
            n = self.graph.matrix[self.y][self.x + 1]
            if self.is_neighbour(n) and self.is_step_allowed(n):
                self.neighbours.append((n, cost))

        if self.y > 0:
            n = self.graph.matrix[self.y - 1][self.x]
            if self.is_neighbour(n) and self.is_step_allowed(n):
                self.neighbours.append((n, cost))

        if self.y < len(self.graph.matrix) - 1:
            n = self.graph.matrix[self.y + 1][self.x]
            if self.is_neighbour(n) and self.is_step_allowed(n):
                self.neighbours.append((n, cost))

    def is_neighbour(self, other) -> bool:
        return (self.x == other.x and abs(self.y - other.y) == 1) or (self.y == other.y and abs(self.x - other.x) == 1)

    def is_step_allowed(self, other) -> bool:
        return ord(other.text) - ord(self.text) <= 1

def create_vertex(v_id, text, x, y, graph) -> Vertex:
    return Vertex(v_id, text, x, y, graph)

class Graph:
    def __init__(self, lines: list[str]) -> None:
        self.matrix = []
        self.vertices = []

        vertex_id = 0
        for y, row in enumerate(lines):
            self.matrix.append([])
            for x, char in enumerate([c for c in row]):
                v = create_vertex(vertex_id, char, x, y, self)
                self.matrix[y].append(v)
                self.vertices.append(v)
                vertex_id += 1

        for v in self.vertices:
            v.compute_neighbours()

    def set_matrix(self, matrix) -> None:
        self.matrix = matrix

    def dijkstra(self):
        distances = {v: float("inf") for v in self.vertices}
        prev_v = {v: None for v in self.vertices}

        source_vertex = next((v for v in self.vertices if v.is_start), None)
        dest_vertex = next((v for v in self.vertices if v.is_end), None)
        assert source_vertex != None and dest_vertex != None

        distances[source_vertex] = 0 # set start to cost 0
        source_vertex.cost_to_start = 0
        heap = [source_vertex] # add start vertex to heap with cost 0

        while heap:
            v = heapq.heappop(heap)

            if v == dest_vertex:
                break

            curr_cost = v.cost_to_start
            if curr_cost > distances[v]: # skip vertex if it has been processed
                continue

            #vertices_copy.remove(v)
            #if (distances[v] == float("inf")):
                #break

            for neighbour, cost in v.get_neighbours():
                path_cost = curr_cost + cost
                
                if path_cost < neighbour.cost_to_start:
                    prev_v[neighbour] = v
                    neighbour.cost_to_start = path_cost
                    heapq.heappush(heap, neighbour)

        path = []
        curr_v = dest_vertex
        while prev_v[curr_v] is not None:
            path.insert(0, curr_v)
            curr_v = prev_v[curr_v]
        
        path.insert(0, curr_v)

        return path

    def print_path(self, path):
        for row in self.matrix:
            for v in row:
                found = v in path
                
                if found == False and v.text != CONST_START and v.text != CONST_END:
                    # not in path
                    output = v.text
                else:
                    # in path: print in bold
                    output = color.CYAN + v.text + color.END

                print(output, end="")
            print()

        print("->".join(p.text for p in path))

with open("./inputs/day12.txt") as file:
    lines = [line.strip() for line in file.readlines()]

    start = time.time()
    graph = Graph(lines)
    end = time.time()
    print("duration setup: " + str(end - start))

    start = time.time()
    path = graph.dijkstra()
    end = time.time()

    #graph.print_path(path)
    print("duration calc: " + str(end - start))
    print("length: " + str(len(path) - 1))
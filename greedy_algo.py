from queue import PriorityQueue
# import sys​


vertex_distance = []
parent_vertexes = []

class Ghaph:
    def __init__(self):
        self.vertexes = dict()
        self.edges = []


    def add_edge(self, from_vertex_name: int, to_vertex_name: int, 
    from_vertex_x_coord = 0, from_vertex_y_coord = 0, 
    to_vertex_x_coord = 0, to_vertex_y_coord = 0, weight = 0):

        # check if vertex is already known
        # create new if not

        from_vertex = vertexes.get(from_vertex_name) or Vertex(from_vertex_x_coord, from_vertex_y_coord, from_vertex_name)
        self.vertexes[from_vertex_name] = from_vertex
        to_vertex = vertexes.get(to_vertex_name) or Vertex(to_vertex_x_coord, to_vertex_y_coord, to_vertex_name)
        self.vertexes[to_vertex_name] = to_vertex

        edge = Edge(from_vertex, to_vertex, weight)
        self.edges.append(edge)
        # if graph is oriented
        from_vertex.add_edge(edge)


​
class Vertex:
    def __init__(self, x, y, name):
        self.name = name
        self.x_coord = x
        self.y_coord = y
        self.edges = []
    
    def add_edge(self, edge: Edge):
        self.edges.append(edge)


class Edge:
    def __init__(self, from_vertex: Vertex, to_vertex: Vertex, weight = 0):
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex
        self.weight = weight


def dejkstra(graph: list, start_vertex: int):
    init_graph_vars(graph, start_vertex)
​
    # we need to have priority queue to store available nodes
    #and pickup the one with lowest weight
    # it stores the tuples (distance_to_it, vertex)
    # in such priority that vertex with lowest distance is on
    # position 0
    available_vertexes_queue = PriorityQueue()
    available_vertexes_queue.put((0,start_vertex))
​
    # infinite cycle right now
    # available_vertexes_queue: (159, 5)
    while not available_vertexes_queue.empty():
        vertex_to_check = available_vertexes_queue.get()[1]
​
        for child_vertex_tuple in graph[vertex_to_check]:
            child_vertex = child_vertex_tuple[0]
            distance = vertex_distance[vertex_to_check] + child_vertex_tuple[1]
            if relax_edge(child_vertex, vertex_to_check, distance):
                available_vertexes_queue.put((distance,child_vertex))
        print(vertex_to_check)
​
def relax_edge(child_vertex, parent_vertex, distance):
    '''
    stores the distance between two vertexes and parent one
    for the passed child
    '''
    if (vertex_distance[child_vertex] <  distance):
        return False
    parent_vertexes[child_vertex] = parent_vertex
    vertex_distance[child_vertex] = distance
    return True
​
​
​
def init_graph_vars(graph: list, start_vertex: int):
​
    for vertex in graph:
        vertex_distance.append(sys.maxsize)
        parent_vertexes.append(None)
    vertex_distance[start_vertex] = 0
​
    #parent_vertexes[0] - None
    #parent_vertexes[1] - 0 the vertex from which we come to v_1
    #parent_vertexes[2] - 0
    #parent_vertexes[3] - 2
    #parent_vertexes[4] - 1
    #parent_vertexes[5] - 4
​
def belman_ford(graph: list, start_vertex: int):
    init_graph_vars(graph, start_vertex)
​
    # defines relax tries count
    for i in range(len(graph) - 1):
        belman_ford_relax(graph)
​
    # try to relax one more time and if result is True - we have negative cycle
    if belman_ford_relax(graph):
        print("we have cycle")
​
def belman_ford_relax():
    at_least_once_relaxed = False
    for current_vertex_number in range(len(graph)):
        vertex_edges = graph[current_vertex_number]
        for edge in vertex_edges:
            child_vertex = edge[0]
            distance = vertex_distance[current_vertex_number] + edge[1]
            if relax_edge(child_vertex, current_vertex_number, distance):
                at_least_once_relaxed = True
​
    if not at_least_once_relaxed:
        return True #means no negative cycle
​
dejkstra([
            [ (1, 99),(2, 50) ],
            [ (4, 50), (3, 50), (2, 50) ],
            [ (3, 99) ],
            [ (4, 75) ],
            [ (5, 10) ],
            []
        ], 0)
print(vertex_distance)
#-->
#1 - 99
#2 - 50
#3 - 149
#4 - 149
#10 - 159


def greedy_first_search(graph: list, start_vertex: int):
    init_graph_vars(graph, start_vertex)
​
    # we need to have priority queue to store available nodes
    #and pickup the one with lowest weight
    # it stores the tuples (distance_to_it, vertex)
    # in such priority that vertex with lowest distance is on
    # position 0


    available_vertexes_queue = PriorityQueue()
    available_vertexes_queue.put((0,start_vertex))
​
    # infinite cycle right now
    # available_vertexes_queue: (159, 5)
    while not available_vertexes_queue.empty():
        vertex_to_check = available_vertexes_queue.get()[1]
        for child_vertex_tuple in graph[vertex_to_check]:
            child_vertex = child_vertex_tuple[0]
            distance = vertex_distance[vertex_to_check] + child_vertex_tuple[1]
            estimated_distance_to_destination = calculate_estimated_distance(vertex_to_check, end_vertex)
            if (vertex_distance[child_vertex] >  estimated_distance_to_destination):
                parent_vertexes[child_vertex] = vertex_to_check
                vertex_distance[child_vertex] = distance
                # distance + estimated_distance_to_destination because it's really needed
                # for better performance
                available_vertexes_queue.put((distance + estimated_distance_to_destination,child_vertex))
        print(vertex_to_check)


def calculate_estimated_distance(from_vertex, to_vertex):
    # will not work
    return abs(from_vertex.x - to_vertex.x) + abs(from_vertex.y - to_vertex.y)
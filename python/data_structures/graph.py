class Graph:

    def __init__(self):
        self.vertices_list = []
        self._vertices_list = {}

    def add_node(self, value):
        vertex = Vertex(value)
        if vertex not in self.vertices_list:
            self.vertices_list.append(vertex)
            return vertex

    def add_edge(self, v1, v2, weight=1):
        if v1 in self.vertices_list and v2 in self.vertices_list:
            edge = Edge(v2, weight)
            v1.adjacent_list.append([v2, edge])
        else:
            raise (KeyError)

    def get_nodes(self):
        return self.vertices_list

    def get_neighbors(self, vertex):
        neighbors = []
        for item in self.vertices_list:
            if item.value == vertex.value:
                for edges in item.adjacent_list:
                    neighbors.append(edges[1])
        return neighbors

    def size(self):
        return len(self.vertices_list)

    def depth_first_search(self, Graph):
        viseted = {}
        collection = []
        root_vertex = Graph._vertices_list.keys()[0]

        def traversal(vertex_root):
            nonlocal viseted, collection, Graph
            if vertex_root == None:
                return "empty"

            if vertex_root not in viseted:
                collection.append(vertex_root)
                viseted[vertex_root] = True
            if Graph._vertices_list.get(vertex_root):
                for last_vertex in Graph._vertices_list.get(root_vertex):
                    traversal(last_vertex)

        traversal(root_vertex)
        return collection


class Vertex:
    '''
    Vertex represents the individual Nodes inside the graph.
    The attribute value represents the stored data.
    The list of neighbors attribute represents the vertices with which exists a connection.
    '''

    def __init__(self, value):
        self.value = value
        self.adjacent_list = []
        self._vertices_list = {}


class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight

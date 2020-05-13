from util import Stack

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('that vertex does not exist')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create an empty stack
        ss = Stack()
        # path to starting vertex
        ss.push([starting_vertex])
        # set for visited vetices
        visited = set()
        # while path is not empty
        while ss.size() > 0:
            # pop the first path
            path = ss.pop()
            # take last vertex in path
            path_last_vertex = path[-1]
            # if we havent been there yet
            if path_last_vertex not in visited:
                # check if current is the destination
                if path_last_vertex == destination_vertex:
                    # return the path if it is
                    return path
                # mark as visited if it is not
                else:
                    # get the neighbors / make new versions on the path
                    visited.add(path_last_vertex)
                    neighbors = self.get_neighbors(path_last_vertex)
                    for neighbor in neighbors:
                        # duplicate the path
                        new_path = path[:]
                        # add the neighbor
                        new_path.append(neighbor)
                        # add the new path
                        ss.push(new_path)


def earliest_ancestor(ancestors, starting_node):
    # create graph
    ancestor_graph = Graph()
    # create path
    paths = []

    # add verticies to graph
    for vertex in range(0, 20):
        ancestor_graph.add_vertex(vertex)

    # add edges to graph
    for ancestor in ancestors:
        ancestor_graph.add_edge(ancestor[0], ancestor[1])

    # add path to ancestor paths
    for vertex in ancestor_graph.vertices:
        if ancestor_graph.dfs(vertex, starting_node) is not None and len(ancestor_graph.dfs(vertex, starting_node)) > 0:
            paths.append(ancestor_graph.dfs(vertex, starting_node))

    if len(paths) == 1:
        return -1

    # find earliest neighbor
    start_path = paths[0]
    for path in paths:
        if len(path) > len(start_path) or len(start_path) and path[0] < start_path[0]:
            start_path = path

    return start_path[0]
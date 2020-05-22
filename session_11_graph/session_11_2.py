graph_sample = {
    'a': ['c'],
    'b': ['c', 'e'],
    'c': ['a', 'b', 'd', 'e'],
    'd': ['c'], 
    'e': ['c', 'b'],
    'f': [],
}

class Graph:
    def __init__(self, graph_dict = {}):
        self.graph_dict = graph_dict

    def vertices(self):
        '''returns the vertices of a graph'''
        return list(self.graph_dict.keys())

    def edges(self):
        '''returns the edges of a graph'''
        return self.generate_edges()
    
    def add_vertex(self, vertex):
        '''If the vertex 'vertex' is not in self.graph_dict, 
           a key 'vertex' with an empty list as a value is added
           to the dictionary.
           Otherwise nothing has to be done'''

        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph_dict:
            self.graph_dict[vertex1].append(vertex2)
        else:
            self.graph_dict[vertex1] = [vertex2]
        
            
    def generate_edges(self):
        '''A static method generating the edges of the graph 'graph'
        '''        
        edges = []
        for vertex in self.graph_dict:
            for neighbour in self.graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        res = 'vertices: '
        for k in self.graph_dict:
            res += str(k) + ' '
        res += '\nedges: '
        for edge in self.generate_edges():
            res += str(edge) + ' '
        return res

g = Graph()
print(g)
g.add_vertex('a')
g.add_edge('b','a')
g.add_vertex('c')
g.add_edge('d','f')
print(g)
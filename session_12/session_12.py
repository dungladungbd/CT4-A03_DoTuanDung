# DFS: Depth First Search
# BFS: Breadth First Search

graph_sample = {
    'a': ['c'],
    'b': ['c', 'e'],
    'c': ['a', 'b', 'd', 'e'],
    'd': ['c'],
    'e': ['c', 'b'],
    'f': [],
}
graph_sample_2 = {
    "a": ['b', 'c'],
    'b': ['d', 'e'],
    'c': ['f', 'g'],
    'd': [],
    'e': ['h', 'i', 'k'],
    'f': ['m', 'l'],
    'g': [],
    'h': [],
    'i': [],
    'k': [],
    'l': ['o', 'p'],
    'm': ['q', 'r'],
    'o': [],
    'p': [],
    'q': [],
    'r': [],
}
graph_sample_3 = {
    'a': ['b', 'c', 'd'],
    'b': ['f'],
    'c': ['a', 'o'],
    'd': [],
    'f': ['o'],
    'o': ['f'],
}


class Graph:
    def __init__(self, graph_dict={}):
        self.graph_dict = graph_dict

    def vertices(self):
        return list(self.graph_dict.keys())

    def edges(self):
        return self.generate_edges()

    def add_vertex(self, vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph_dict:
            self.graph_dict[vertex1].append(vertex2)
        else:
            self.graph_dict[vertex1] = [vertex2]

    def generate_edges(self):
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

    def BFS(self, vertex):
        search_list = [vertex]
        loop = True
        while loop:
            a = len(search_list)
            for i in search_list:
                for j in self.graph_dict[i]:
                    if j not in search_list:
                        search_list.append(j)
            if a == len(search_list):
                loop = False
        return search_list

    def BFS_2(self, vertex):
        visited = []
        queue = []
        queue.append(vertex)
        visited.append(vertex)
        while queue:
            vertex = queue.pop(0)
            for i in self.graph_dict[vertex]:
                queue.append(i)
                visited.append(i)
        return visited

    def DFS(self, vertex):
        search_list = []
        self.DFS_util(vertex, search_list)
        return search_list

    def DFS_util(self, vertex, search_list):
        search_list.append(vertex)
        for i in self.graph_dict[vertex]:
            if i not in search_list:
                self.DFS_util(i, search_list)

    def shortest_path(self, start, goal):
        path = [goal]
        self.s_p_sp(start, goal, path)
        return path

    def s_p_sp(self, start, goal, path):
        if goal == start:
            return path
        visited = []
        queue = []
        queue.append(start)
        visited.append(start)
        while queue:
            vertex = queue.pop()
            for i in self.graph_dict[vertex]:
                queue.insert(0, i)
                visited.insert(0, i)
            if goal in visited:
                path.insert(0, vertex)
                goal = vertex
                queue = False
        self.s_p_sp(start, goal, path)
        return path

        


sample = Graph(graph_sample_3)
# print(sample.BFS('a'))

# print(sample.DFS('a'))
print(sample.shortest_path('a', 'o'))

class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        # print("Graph dict", self.graph

    def get_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []
        paths = []
        new_path = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_path = self.get_path(node, end, path)
                for p in new_path:
                    paths.append(p)
        return paths

routes = [
    ("Mumbai", "Paris"),
    ("Mumbai", "Dubai"),
    ("Paris", "Dubai"),
    ("Paris","New York"),
    ("Dubai", "New York"),
    ("New York", "Toronto"),
    ("China", "Japan"),
]

route_graph = Graph(routes)
start = "Paris"
end = "New York"
print(f"Path between {start} and {end} :",route_graph.get_path(start, end) )
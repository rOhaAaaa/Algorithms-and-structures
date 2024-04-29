from collections import defaultdict, deque
import pandas as pd

class Graph:
    def __init__(self):
        self.graph = defaultdict(lambda: defaultdict(int))

    def add_edge(self, u, v, w):
        self.graph[u][v] = w

    def bfs(self, source, sink, parent):
        visited = set()
        queue = deque([source])
        visited.add(source)

        while queue:
            u = queue.popleft()

            for ind in self.graph[u]:
                if ind not in visited and self.graph[u][ind] > 0:
                    queue.append(ind)
                    visited.add(ind)
                    parent[ind] = u
                    if ind == sink:
                        return True
        return False

    def ford_fulkerson(self, source, sink):
        parent = {}
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float('Inf')
            s = sink

            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

            max_flow += path_flow

        return max_flow

file_path = r'C:\Users\Acer\Documents\ПРОГРАМУВАННЯ 1 курс 2 семестр\LABA8\roads.csv'  
data = pd.read_csv(file_path)

g = Graph()
for index, row in data.iterrows():
    g.add_edge(row['Start'], row['End'], row['Capacity'])

farms = ['F1', 'F2', 'F3']
stores = ['S1', 'S2', 'S3', 'S4', 'S5']
super_source = 'SuperSource'
super_sink = 'SuperSink'

for farm in farms:
    g.add_edge(super_source, farm, float('Inf'))

for store in stores:
    g.add_edge(store, super_sink, float('Inf'))

max_flow = g.ford_fulkerson(super_source, super_sink)
print(f"Максимальна кількість автомобілів, які зможуть проїхати протягом дня з квіткових ферм до квіткових магазинів: {max_flow}")

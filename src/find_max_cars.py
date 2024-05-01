from collections import defaultdict, deque
import pandas as pd
from typing import Dict, Set, Deque, List

class Graph:
    def __init__(self) -> None:
        """
        Initializes the graph as a nested dictionary where each node maps to another node with an integer weight.
        """
        self.graph: Dict[str, Dict[str, int]] = defaultdict(lambda: defaultdict(int))

    def add_edge(self, u: str, v: str, w: int) -> None:
        """
        Adds an edge to the graph with a specified weight.

        Parameters:
        u (str): The starting node of the edge.
        v (str): The ending node of the edge.
        w (int): The weight of the edge, representing the maximum flow capacity.
        """
        self.graph[u][v] = w

    def bfs(self, source: str, sink: str, parent: Dict[str, str]) -> bool:
        """
        Performs the Breadth-First Search (BFS) to find a path from source to sink.

        Parameters:
        source (str): The source node for the BFS.
        sink (str): The target node for the BFS.
        parent (Dict[str, str]): Dictionary to store the path of nodes.

        Returns:
        bool: True if a path exists from source to sink, False otherwise.
        """
        visited: Set[str] = set()
        queue: Deque[str] = deque([source])
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

    def ford_fulkerson(self, source: str, sink: str) -> int:
        """
        Computes the maximum flow from source to sink using the Ford-Fulkerson method.

        Parameters:
        source (str): The source node where the flow starts.
        sink (str): The sink node where the flow ends.

        Returns:
        int: The maximum flow from source to sink.
        """
        parent: Dict[str, str] = {}
        max_flow: int = 0

        while self.bfs(source, sink, parent):
            path_flow: int = float('Inf')
            s: str = sink

            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            v: str = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

            max_flow += path_flow

        return max_flow

file_path: str = r'C:\Users\Acer\Documents\ПРОГРАМУВАННЯ 1 курс 2 семестр\LABA8\roads.csv'  
data = pd.read_csv(file_path)

g = Graph()
for index, row in data.iterrows():
    g.add_edge(row['Start'], row['End'], row['Capacity'])

farms: List[str] = ['F1', 'F2', 'F3']
stores: List[str] = ['S1', 'S2', 'S3', 'S4', 'S5']
super_source: str = 'SuperSource'
super_sink: str = 'SuperSink'

for farm in farms:
    g.add_edge(super_source, farm, float('Inf'))

for store in stores:
    g.add_edge(store, super_sink, float('Inf'))

max_flow: int = g.ford_fulkerson(super_source, super_sink)
print(f"Максимальна кількість автомобілів, які зможуть проїхати протягом дня з квіткових ферм до квіткових магазинів: {max_flow}")

from collections import defaultdict, deque
import pandas as pd
from typing import Dict, Set, Deque, List, Tuple

class Graph:
    def __init__(self) -> None:
        """
        Initializes the graph as a nested dictionary where each node maps to another node with an integer weight.
        """
        self.graph: Dict[str, Dict[str, int]] = defaultdict(lambda: defaultdict(int))

    def add_edge(self, start_node: str, end_node: str, weight: int) -> None:
        """
        Adds an edge to the graph with a specified weight.

        Parameters:
        start_node (str): The starting node of the edge.
        end_node (str): The ending node of the edge.
        weight (int): The weight of the edge, representing the maximum flow capacity.
        """
        self.graph[start_node][end_node] = weight

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
            current_node = queue.popleft()

            for neighbor_node in self.graph[current_node]:
                if neighbor_node not in visited and self.graph[current_node][neighbor_node] > 0:
                    queue.append(neighbor_node)
                    visited.add(neighbor_node)
                    parent[neighbor_node] = current_node
                    if neighbor_node == sink:
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
            current_node: str = sink

            while current_node != source:
                path_flow = min(path_flow, self.graph[parent[current_node]][current_node])
                current_node = parent[current_node]

            current_sink: str = sink
            while current_sink != source:
                current_source = parent[current_sink]
                self.graph[current_source][current_sink] -= path_flow
                self.graph[current_sink][current_source] += path_flow
                current_sink = parent[current_sink]

            max_flow += path_flow

        return max_flow


def read_graph_and_nodes_from_csv(file_path: str) -> Tuple[Graph, List[str], List[str]]:
    """
    Reads a graph structure from a CSV file and creates the graph object.

    Parameters:
    file_path (str): The path to the CSV file containing the graph data.

    Returns:
    Graph: The graph object constructed from the CSV data.
    List[str]: List of farm nodes.
    List[str]: List of store nodes.
    """
    with open(file_path) as f:
        farms = f.readline().strip().split(',')
        stores = f.readline().strip().split(',')

    data = pd.read_csv(file_path, skiprows=[0, 1])

    g = Graph()

    for start_node, end_node, weight in data.itertuples(index=False):
        g.add_edge(start_node, end_node, weight)

    return g, farms, stores


def find_max_flow(file_path: str) -> int:
    """
    Finds the maximum flow of cars that can travel from the flower farms to the stores in one day.

    Parameters:
    file_path (str): The path to the CSV file containing the graph data.

    Returns:
    int: The maximum number of cars that can travel from the farms to the stores in one day.
    """
    g, farms, stores = read_graph_and_nodes_from_csv(file_path)

    super_source = 'SuperSource'
    super_sink = 'SuperSink'

    for farm in farms:
        g.add_edge(super_source, farm, float('Inf'))

    for store in stores:
        g.add_edge(store, super_sink, float('Inf'))

    return g.ford_fulkerson(super_source, super_sink)


if __name__ == '__main__':
    file_path = r'C:\Users\Acer\Documents\ПРОГРАМУВАННЯ 1 курс 2 семестр\LABA8\roads.csv'
    max_flow = find_max_flow(file_path)
    print(f"Максимальна кількість автомобілів, які зможуть проїхати протягом дня з квіткових ферм до квіткових магазинів: {max_flow}")

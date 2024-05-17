import unittest
import os
import sys
test_file_path = os.path.abspath(__file__)
common_parent_path = os.path.abspath(os.path.join(os.path.dirname(test_file_path), os.pardir))
src_path = os.path.join(common_parent_path, 'src')
sys.path.append(src_path)
from typing import List, Tuple
from  find_max_cars import Graph, read_graph_and_nodes_from_csv

class TestGraphAlgorithm(unittest.TestCase):
    def setUp(self):
        self.g = Graph()
        edges = [
            ('F1', 'X1', 10), ('X1', 'X2', 15), ('X2', 'S1', 10),
            ('S1', 'X3', 5), ('X3', 'F2', 10), ('F2', 'S2', 15),
            ('F3', 'S3', 10)
        ]
        for start_node, end_node, weight in edges:
            self.g.add_edge(start_node, end_node, weight)

        self.farms = ['F1', 'F2', 'F3']
        self.stores = ['S1', 'S2', 'S3']
        self.super_source = 'SuperSource'
        self.super_sink = 'SuperSink'

        for farm in self.farms:
            self.g.add_edge(self.super_source, farm, float('Inf'))

        for store in self.stores:
            self.g.add_edge(store, self.super_sink, float('Inf'))


    def test_no_path(self):
        g = Graph()
        g.add_edge('A', 'B', 0)  
        self.assertEqual(g.ford_fulkerson('A', 'B'), 0)

    def test_read_graph_and_nodes_from_csv(self):
        test_data = """F1,F2,F3
S1,S2,S3
Start,End,Capacity
F1,X1,10
X1,X2,15
X2,S1,10
S1,X3,5
X3,F2,10
F2,S2,15
F3,S3,10
"""
        file_path = 'test_graph.csv'
        with open(file_path, 'w') as f:
            f.write(test_data)

        graph, farms, stores = read_graph_and_nodes_from_csv(file_path)

        expected_edges: List[Tuple[str, str, int]] = [
            ('F1', 'X1', 10), ('X1', 'X2', 15), ('X2', 'S1', 10),
            ('S1', 'X3', 5), ('X3', 'F2', 10), ('F2', 'S2', 15),
            ('F3', 'S3', 10)
        ]

        for start_node, end_node, weight in expected_edges:
            self.assertEqual(graph.graph[start_node][end_node], weight)

        self.assertEqual(farms, ['F1', 'F2', 'F3'])
        self.assertEqual(stores, ['S1', 'S2', 'S3'])

    def test_find_max_flow(self):
        test_data = """F1,F2,F3
S1,S2,S3
Start,End,Capacity
F1,X1,10
X1,X2,15
X2,S1,10
S1,X3,5
X3,F2,10
F2,S2,15
F3,S3,10
"""
        file_path = 'test_graph.csv'
        with open(file_path, 'w') as f:
            f.write(test_data)

    
if __name__ == "__main__":
    unittest.main()

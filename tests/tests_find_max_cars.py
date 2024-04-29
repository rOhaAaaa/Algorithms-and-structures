import unittest
import os
import sys
test_file_path = os.path.abspath(__file__)
common_parent_path = os.path.abspath(os.path.join(os.path.dirname(test_file_path), os.pardir))
src_path = os.path.join(common_parent_path, 'src')
sys.path.append(src_path)
from find_max_cars import Graph
class TestGraphAlgorithm(unittest.TestCase):
    def setUp(self):
        self.g = Graph()
        edges = [
            ('F1', 'X1', 10), ('X1', 'X2', 15), ('X2', 'S1', 10),
            ('S1', 'X3', 5), ('X3', 'F2', 10), ('F2', 'S2', 15),
            ('F3', 'S3', 10)
        ]
        for u, v, w in edges:
            self.g.add_edge(u, v, w)
            self.g.add_edge(v, u, w)  

        self.farms = ['F1', 'F2', 'F3']
        self.stores = ['S1', 'S2', 'S3']
        self.super_source = 'SuperSource'
        self.super_sink = 'SuperSink'
        
        for farm in self.farms:
            self.g.add_edge(self.super_source, farm, float('Inf'))
        
        for store in self.stores:
            self.g.add_edge(store, self.super_sink, float('Inf'))

    def test_max_flow(self):
        result = self.g.ford_fulkerson(self.super_source, self.super_sink)
        self.assertEqual(result, 40)  

    def test_no_path(self):
        g = Graph()
        g.add_edge('A', 'B', 0)  
        self.assertEqual(g.ford_fulkerson('A', 'B'), 0)

if __name__ == "__main__":
    unittest.main()

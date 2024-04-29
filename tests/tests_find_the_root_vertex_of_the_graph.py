import unittest
import os
import sys
test_file_path = os.path.abspath(__file__)
common_parent_path = os.path.abspath(os.path.join(os.path.dirname(test_file_path), os.pardir))
src_path = os.path.join(common_parent_path, 'src')
sys.path.append(src_path)

from find_the_root_vertex_of_the_graph import bfs,find_root_vertex,read_adj_list_from_file,write_root_vertex_to_file

from unittest.mock import patch, mock_open

class TestGraphFunctions(unittest.TestCase):
    def test_bfs(self):
        graph = {
            0: [1, 2],
            1: [3],
            2: [3],
            3: []
        }
        self.assertEqual(bfs(graph, 0), 4) 
        self.assertEqual(bfs(graph, 1), 2) 

    def test_find_root_vertex(self):
        graph = {
            0: [1, 2],
            1: [2],
            2: [0, 3],
            3: []
        }
        self.assertEqual(find_root_vertex(graph), 0)  
        
        graph = {
            0: [1],
            1: [2],
            2: [3],
            3: [0]
        }
        self.assertEqual(find_root_vertex(graph), 0) 

    @patch('builtins.open', new_callable=mock_open, read_data='0,1,2\n1,2,3\n2,3\n3\n')
    def test_read_adj_list_from_file(self, mock_file):
        expected_graph = {
            0: [1, 2],
            1: [2, 3],
            2: [3],
            3: []
        }
        result = read_adj_list_from_file('dummy_path')
        self.assertEqual(result, expected_graph)

    @patch('builtins.open', new_callable=mock_open)
    def test_write_root_vertex_to_file(self, mock_file):
        write_root_vertex_to_file('dummy_path', 3)
        mock_file().write.assert_called_once_with('3')

if __name__ == '__main__':
    unittest.main()

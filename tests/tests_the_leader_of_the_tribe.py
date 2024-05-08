import unittest
from unittest.mock import mock_open, patch
import sys
from io import StringIO
import os
test_file_path = os.path.abspath(__file__)
common_parent_path = os.path.abspath(os.path.join(os.path.dirname(test_file_path), os.pardir))
src_path = os.path.join(common_parent_path, 'src')
sys.path.append(src_path)
from the_leader_of_the_tribe import solve  
class TestMarriageSolver(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data="3\n1 2\n2 4\n3 5\n")
    def test_basic_input(self, mock_file):
        expected_output = "4\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            solve("dummy_path")
            self.assertEqual(fake_out.getvalue(), expected_output)

    @patch('builtins.open', new_callable=mock_open, read_data="5\n1 2\n2 4\n1 3\n3 5\n8 10\n")
    def test_more_complex_input(self, mock_file):
        expected_output = "6\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            solve("dummy_path")
            self.assertEqual(fake_out.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()

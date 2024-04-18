import unittest
from unittest.mock import mock_open, patch
import sys
from io import StringIO
from LABA6 import solve  
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

import unittest
import os
import sys
test_file_path = os.path.abspath(__file__)
common_parent_path = os.path.abspath(os.path.join(os.path.dirname(test_file_path), os.pardir))
src_path = os.path.join(common_parent_path, 'src')
sys.path.append(src_path)
from find_kth_largest import find_kth_largest

class TestFindKthLargest(unittest.TestCase):
    def test_first_largest(self):
        self.assertEqual(find_kth_largest([3, 2, 1, 5, 6, 4], 1), 6, "Should be 6")

    def test_third_largest(self):
        self.assertEqual(find_kth_largest([3, 2, 1, 5, 6, 4], 3), 4, "Should be 4")

if __name__ == '__main__':
    unittest.main()

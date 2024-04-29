import unittest
import os
import sys
test_file_path = os.path.abspath(__file__)
common_parent_path = os.path.abspath(os.path.join(os.path.dirname(test_file_path), os.pardir))
src_path = os.path.join(common_parent_path, 'src')
sys.path.append(src_path)
from find_last_occurrence import find_last_occurrence
class TestStringMethods(unittest.TestCase):
    
    def test_basic(self):
        haystack = "hello world, hello sea, hello sky"
        needle = "hello"
        self.assertEqual(find_last_occurrence(haystack, needle), (28, 41))

    def test_no_occurrence(self):
        haystack = "hello world, hello sea, hello sky"
        needle = "sun"
        self.assertEqual(find_last_occurrence(haystack, needle), (-1, 33))

    def test_needle_longer_than_haystack(self):
        haystack = "hello"
        needle = "hello world, hello sea, hello sky"
        self.assertEqual(find_last_occurrence(haystack, needle), (-1, 0))
         
    def test_empty_needle(self):
        haystack = "hello world, hello sea, hello sky"
        needle = ""
        self.assertEqual(find_last_occurrence(haystack, needle), (-1, 0))

    def test_empty_haystack(self):
        haystack = ""
        needle = "hello"
        self.assertEqual(find_last_occurrence(haystack, needle), (-1, 0))


if __name__ == '__main__':
    unittest.main()

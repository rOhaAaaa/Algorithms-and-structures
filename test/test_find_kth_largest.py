import unittest

class TestFindKthLargest(unittest.TestCase):
    def test_first_largest(self):
        self.assertEqual(find_kth_largest([3, 2, 1, 5, 6, 4], 1), 6, "Should be 6")

    def test_third_largest(self):
        self.assertEqual(find_kth_largest([3, 2, 1, 5, 6, 4], 3), 4, "Should be 4")

if __name__ == '__main__':
    unittest.main()

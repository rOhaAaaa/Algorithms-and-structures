import unittest
import os
import sys
test_file_path = os.path.abspath(__file__)
common_parent_path = os.path.abspath(os.path.join(os.path.dirname(test_file_path), os.pardir))
src_path = os.path.join(common_parent_path, 'src')
sys.path.append(src_path)
from jeki_eats_bananas import min_eating_speed

from jeki_eats_bananas import min_eating_speed

class TestBananaEatingSpeed(unittest.TestCase):

    def test_min_eating_speed(self):
        self.assertEqual(min_eating_speed([3,6,7,11], 8), 4)
        self.assertEqual(min_eating_speed([30,11,23,4,20], 5), 30)
        self.assertEqual(min_eating_speed([30,11,23,4,20], 6), 23)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)

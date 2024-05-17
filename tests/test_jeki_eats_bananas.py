import unittest
import os
import sys

script_dir = os.path.dirname(os.path.relpath(__file__))
sys.path.append(os.path.dirname(script_dir))
sys.path.append(src_path)
from src.jeki_eats_bananas import min_eating_speed

class TestBananaEatingSpeed(unittest.TestCase):

    def test_min_eating_speed(self):
        self.assertEqual(min_eating_speed([3,6,7,11], 8), 4)
        self.assertEqual(min_eating_speed([30,11,23,4,20], 5), 30)
        self.assertEqual(min_eating_speed([30,11,23,4,20], 6), 23)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)

import unittest
import os
import sys
test_file_path = os.path.abspath(__file__)
common_parent_path = os.path.abspath(os.path.join(os.path.dirname(test_file_path), os.pardir))
src_path = os.path.join(common_parent_path, 'src')
sys.path.append(src_path)

from the_length_of_the_max_chain import can_transform, max_chain_length

class TestWordChainGame(unittest.TestCase):
    def test_can_transform(self):
        self.assertTrue(can_transform('crates', 'crate'))
        self.assertTrue(can_transform('crate', 'rate'))
        self.assertFalse(can_transform('crate', 'carte'))
        self.assertFalse(can_transform('a', 'a'))

    def test_max_chain_length(self):
        words_1 = ['crates', 'car', 'cats', 'crate', 'rate', 'at', 'ate', 'tea', 'rat', 'a']
        self.assertEqual(max_chain_length(words_1), 6)  
        
        words_2 = ['b', 'bcad', 'bca', 'bad', 'bd']
        self.assertEqual(max_chain_length(words_2), 4)
        
        words_3 = ['word', 'anotherword', 'yetanotherword']
        self.assertEqual(max_chain_length(words_3), 1)  

if __name__ == '__main__':
    unittest.main()

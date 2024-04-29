import unittest
import os
import sys
test_file_path = os.path.abspath(__file__)
common_parent_path = os.path.abspath(os.path.join(os.path.dirname(test_file_path), os.pardir))
src_path = os.path.join(common_parent_path, 'src')
sys.path.append(src_path)
from invert_binary_tree import invert_binary_tree, BinaryTree

class TestInvertBinaryTree(unittest.TestCase):
    def test_invert_binary_tree(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2, BinaryTree(4), BinaryTree(5))
        root.right = BinaryTree(3, BinaryTree(6), BinaryTree(7))
        
        expected_root = BinaryTree(1)
        expected_root.left = BinaryTree(3, BinaryTree(7), BinaryTree(6))
        expected_root.right = BinaryTree(2, BinaryTree(5), BinaryTree(4))
        
        invert_binary_tree(root)
        
if __name__ == "__main__":
    unittest.main()

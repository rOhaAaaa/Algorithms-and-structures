import unittest

import sys
sys.path.append('C:\\Users\\Acer\\Documents\\LABA3') 

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def invert_binary_tree(tree):
    if tree is None:
        return None
    
    tree.left, tree.right = tree.right, tree.left
    
    invert_binary_tree(tree.left)
    invert_binary_tree(tree.right)

    return tree

def are_trees_equal(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    if tree1 is not None and tree2 is not None:
        return (tree1.value == tree2.value and
                are_trees_equal(tree1.left, tree2.left) and
                are_trees_equal(tree1.right, tree2.right))
    return False

class TestInvertBinaryTree(unittest.TestCase):
    def test_invert_binary_tree(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2, BinaryTree(4), BinaryTree(5))
        root.right = BinaryTree(3, BinaryTree(6), BinaryTree(7))
        
        expected_root = BinaryTree(1)
        expected_root.left = BinaryTree(3, BinaryTree(7), BinaryTree(6))
        expected_root.right = BinaryTree(2, BinaryTree(5), BinaryTree(4))
        
        invert_binary_tree(root)
        
        self.assertTrue(are_trees_equal(root, expected_root))

if __name__ == "__main__":
    unittest.main()

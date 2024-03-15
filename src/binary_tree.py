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

root = BinaryTree(1)
root.left = BinaryTree(2, BinaryTree(4), BinaryTree(5))
root.right = BinaryTree(3, BinaryTree(6), BinaryTree(7))

invert_binary_tree(root)

def preorder_traversal(node):
    if node is not None:
        print(node.value, end=" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)

print("Попередній обхід інвертованого дерева:")
preorder_traversal(root)


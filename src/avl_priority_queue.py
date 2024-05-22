class Node:
    def __init__(self, value, priority, left=None, right=None):
        self.value = value
        self.priority = priority
        self.left = left
        self.right = right
        self.height = 1

class AVLPriorityQueue:
    def __init__(self):
        self.root = None

    def insert(self, value, priority):
        self.root = self._insert(self.root, value, priority)

    def _insert(self, node, value, priority):
        if not node:
            return Node(value, priority)
        elif priority < node.priority:  
            node.left = self._insert(node.left, value, priority)
        else:
            node.right = self._insert(node.right, value, priority)

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        return self._balance(node)
    
    def _balance(self, node):
        if not node:
            return node
        balance = self._height(node.left) - self._height(node.right)
        if balance > 1:
            if self._height(node.left.left) >= self._height(node.left.right):
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)
        if balance < -1:
            if self._height(node.right.right) >= self._height(node.right.left):
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)
        return node

    def _rotate_left(self, z):
        y = z.right
        A = y.left
        y.left = z
        z.right = A
        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        return y

    def _rotate_right(self, y):
        x = y.left
        B = x.right
        x.right = y
        y.left = B
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        x.height = 1 + max(self._height(x.left), self._height(x.right))
        return x

    def _height(self, node):
        if not node:
            return 0
        return node.height
    
    def remove(self):
        if not self.root:
            return None
        self.root, value = self._remove(self.root)
        return value

    def _remove(self, node):
        if node.left is None:
            return node.right, node.value
        node.left, value = self._remove(node.left)
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        return self._balance(node), value

    def peek(self):
        if not self.root:
            return None
        return self.root.value

    def traverse(self, node=None):
        if node is None:
            node = self.root
            if node is None:  
                return []

        result = [node.value]
        if node.left is not None:  
            result.extend(self.traverse(node.left))
        if node.right is not None:  
            result.extend(self.traverse(node.right))

        return result

queue = AVLPriorityQueue()
queue.insert(5, 1)
queue.insert(9, 2)
queue.insert(3, 0)
queue.insert(7, 1)

print("Черга після вставки елементів:")
print(queue.traverse())

print("Елемент з найвищим пріоритетом:", queue.peek())

removed_element = queue.remove()
print("Видалений елемент з найвищим пріоритетом:", removed_element)

print("Черга після видалення елемента:")
print(queue.traverse())

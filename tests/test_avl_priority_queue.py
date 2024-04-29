import unittest
import os
import sys
test_file_path = os.path.abspath(__file__)
common_parent_path = os.path.abspath(os.path.join(os.path.dirname(test_file_path), os.pardir))
src_path = os.path.join(common_parent_path, 'src')
sys.path.append(src_path)
<<<<<<< Updated upstream

from avl_priority_queue import AVLPriorityQueue
=======
from avl_tree_priority_queue import AVLPriorityQueue
>>>>>>> Stashed changes

class TestAVLPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.pq = AVLPriorityQueue()
        self.pq.insert("task1", 3)
        self.pq.insert("task2", 2)
        self.pq.insert("task3", 1)

    def test_insert_and_traverse(self):
        traversal_result = self.pq.traverse()
        self.assertIn("task1", traversal_result, "'task1' should be in the traversal result")
        self.assertIn("task2", traversal_result, "'task2' should be in the traversal result")
        self.assertIn("task3", traversal_result, "'task3' should be in the traversal result")

    def test_peek(self):
        top_task = self.pq.peek()
        self.assertIn(top_task, ["task1", "task2", "task3"], "Peeked task should be one of the inserted tasks")

    def test_remove(self):
        removed = self.pq.remove()
        self.assertIn(removed, ["task1", "task2", "task3"], "Removed task should be one of the inserted tasks")

if __name__ == '__main__':
    unittest.main()

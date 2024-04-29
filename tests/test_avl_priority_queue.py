import unittest

from avl_tree_priority_queue import AVLPriorityQueue

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

import unittest
from standard.stack import Stack


class StackTest(unittest.TestCase):

    def test_initialization(self):
        stack = Stack()

        self.assertTrue(stack.is_empty())
        self.assertEqual(stack.size(), 0)

    def test_push_single_element(self):
        stack = Stack()

        stack.push(10)

        self.assertFalse(stack.is_empty())
        self.assertEqual(stack.size(), 1)
        self.assertEqual(stack.peek(), 10)

    def test_push_multiple_elements(self):
        stack = Stack()

        stack.push(10)
        stack.push(20)
        stack.push(30)

        self.assertEqual(stack.size(), 3)
        self.assertEqual(stack.peek(), 30)

    def test_push_duplicate_elements(self):
        stack = Stack()

        stack.push(10)
        stack.push(10)
        stack.push(20)

        self.assertEqual(stack.size(), 3)
        self.assertEqual(stack.peek(), 20)

    def test_pop_from_empty_stack(self):
        stack = Stack()

        self.assertIsNone(stack.pop())
        self.assertTrue(stack.is_empty())
        self.assertEqual(stack.size(), 0)

    def test_pop_single_element(self):
        stack = Stack()

        stack.push(10)

        self.assertEqual(stack.pop(), 10)
        self.assertTrue(stack.is_empty())
        self.assertEqual(stack.size(), 0)

    def test_pop_multiple_elements(self):
        stack = Stack()

        stack.push(10)
        stack.push(20)
        stack.push(30)

        self.assertEqual(stack.pop(), 30)
        self.assertEqual(stack.pop(), 20)
        self.assertEqual(stack.pop(), 10)

        self.assertTrue(stack.is_empty())
        self.assertEqual(stack.size(), 0)

    def test_lifo_order(self):
        stack = Stack()

        stack.push(10)
        stack.push(20)
        stack.push(30)

        popped = [
            stack.pop(),
            stack.pop(),
            stack.pop()
        ]

        self.assertEqual(popped, [30, 20, 10])

    def test_peek_does_not_remove(self):
        stack = Stack()

        stack.push(10)
        stack.push(20)

        self.assertEqual(stack.peek(), 20)
        self.assertEqual(stack.size(), 2)
        self.assertEqual(stack.peek(), 20)

    def test_peek_empty_stack(self):
        stack = Stack()

        self.assertIsNone(stack.peek())

    def test_is_empty_after_push_and_pop(self):
        stack = Stack()

        self.assertTrue(stack.is_empty())

        stack.push(10)
        self.assertFalse(stack.is_empty())

        stack.pop()
        self.assertTrue(stack.is_empty())

    def test_size_after_push_and_pop(self):
        stack = Stack()

        self.assertEqual(stack.size(), 0)

        stack.push(10)
        stack.push(20)
        self.assertEqual(stack.size(), 2)

        stack.pop()
        self.assertEqual(stack.size(), 1)

        stack.pop()
        self.assertEqual(stack.size(), 0)

    def test_push_after_emptying_stack(self):
        stack = Stack()

        stack.push(10)
        stack.pop()

        stack.push(20)

        self.assertEqual(stack.size(), 1)
        self.assertEqual(stack.peek(), 20)

    def test_mixed_operations(self):
        stack = Stack()

        stack.push(10)
        stack.push(20)

        self.assertEqual(stack.pop(), 20)

        stack.push(30)
        stack.push(40)

        self.assertEqual(stack.peek(), 40)
        self.assertEqual(stack.size(), 3)

        self.assertEqual(stack.pop(), 40)
        self.assertEqual(stack.pop(), 30)
        self.assertEqual(stack.pop(), 10)

        self.assertTrue(stack.is_empty())


if __name__ == "__main__":
    unittest.main()
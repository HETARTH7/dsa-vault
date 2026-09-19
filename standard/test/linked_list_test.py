import unittest
from standard.linked_list import LinkedList


class LinkedListTest(unittest.TestCase):

    # =========================
    # Empty List
    # =========================

    def test_empty_list(self):
        ll = LinkedList()

        self.assertTrue(ll.is_empty())
        self.assertEqual(ll.size(), 0)
        self.assertIsNone(ll.get(0))
        self.assertFalse(ll.search(10))
        self.assertFalse(ll.remove(10))
        self.assertFalse(ll.remove_at(0))


    # =========================
    # Append
    # =========================

    def test_append_to_empty_list(self):
        ll = LinkedList()
        ll.append(10)

        self.assertEqual(ll.get(0), 10)
        self.assertEqual(ll.size(), 1)
        self.assertFalse(ll.is_empty())


    def test_append_multiple(self):
        ll = LinkedList()

        ll.append(10)
        ll.append(20)
        ll.append(30)

        self.assertEqual(ll.get(0), 10)
        self.assertEqual(ll.get(1), 20)
        self.assertEqual(ll.get(2), 30)
        self.assertEqual(ll.size(), 3)


    # =========================
    # Prepend
    # =========================

    def test_prepend_to_empty_list(self):
        ll = LinkedList()

        ll.prepend(10)

        self.assertEqual(ll.get(0), 10)
        self.assertEqual(ll.size(), 1)


    def test_prepend_multiple(self):
        ll = LinkedList()

        ll.prepend(10)
        ll.prepend(20)
        ll.prepend(30)

        self.assertEqual(ll.get(0), 30)
        self.assertEqual(ll.get(1), 20)
        self.assertEqual(ll.get(2), 10)
        self.assertEqual(ll.size(), 3)


    # =========================
    # Insert
    # =========================

    def test_insert_at_beginning(self):
        ll = LinkedList()

        ll.append(10)
        ll.append(20)
        ll.append(30)

        ll.insert(0, 5)

        self.assertEqual(ll.get(0), 5)
        self.assertEqual(ll.get(1), 10)
        self.assertEqual(ll.get(2), 20)
        self.assertEqual(ll.get(3), 30)


    def test_insert_in_middle(self):
        ll = LinkedList()

        ll.append(10)
        ll.append(20)
        ll.append(30)

        ll.insert(1, 15)

        self.assertEqual(ll.get(0), 10)
        self.assertEqual(ll.get(1), 15)
        self.assertEqual(ll.get(2), 20)
        self.assertEqual(ll.get(3), 30)


    def test_insert_at_end(self):
        ll = LinkedList()

        ll.append(10)
        ll.append(20)
        ll.append(30)

        ll.insert(3, 40)

        self.assertEqual(ll.get(3), 40)
        self.assertEqual(ll.size(), 4)


    def test_insert_into_empty_list(self):
        ll = LinkedList()

        ll.insert(0, 10)

        self.assertEqual(ll.get(0), 10)
        self.assertEqual(ll.size(), 1)


    # =========================
    # Remove by value
    # =========================

    def test_remove_head(self):
        ll = LinkedList()

        ll.append(10)
        ll.append(20)
        ll.append(30)

        self.assertTrue(ll.remove(10))

        self.assertEqual(ll.get(0), 20)
        self.assertEqual(ll.get(1), 30)
        self.assertEqual(ll.size(), 2)


    def test_remove_middle(self):
        ll = LinkedList()

        ll.append(10)
        ll.append(20)
        ll.append(30)

        self.assertTrue(ll.remove(20))

        self.assertEqual(ll.get(0), 10)
        self.assertEqual(ll.get(1), 30)
        self.assertEqual(ll.size(), 2)


    def test_remove_tail(self):
        ll = LinkedList()

        ll.append(10)
        ll.append(20)
        ll.append(30)

        self.assertTrue(ll.remove(30))

        self.assertEqual(ll.get(0), 10)
        self.assertEqual(ll.get(1), 20)
        self.assertEqual(ll.size(), 2)


    def test_remove_missing_value(self):
        ll = LinkedList()

        ll.append(10)
        ll.append(20)

        self.assertFalse(ll.remove(30))

        self.assertEqual(ll.size(), 2)


    def test_remove_only_node(self):
        ll = LinkedList()

        ll.append(10)

        self.assertTrue(ll.remove(10))

        self.assertTrue(ll.is_empty())
        self.assertEqual(ll.size(), 0)


    def test_remove_duplicate_values(self):
        ll = LinkedList()

        ll.append(10)
        ll.append(20)
        ll.append(10)

        self.assertTrue(ll.remove(10))

        self.assertEqual(ll.get(0), 20)
        self.assertEqual(ll.get(1), 10)
        self.assertEqual(ll.size(), 2)


    # =========================
    # Remove at index
    # =========================

    def test_remove_at_head(self):
        ll = LinkedList()

        ll.append(10)
        ll.append(20)
        ll.append(30)

        self.assertTrue(ll.remove_at(0))

        self.assertEqual(ll.get(0), 20)
        self.assertEqual(ll.get(1), 30)


    def test_remove_at_middle(self):
        ll = LinkedList()

        ll.append(10)
        ll.append(20)
        ll.append(30)

        self.assertTrue(ll.remove_at(1))

        self.assertEqual(ll.get(0), 10)
        self.assertEqual(ll.get(1), 30)


    def test_remove_at_tail(self):
        ll = LinkedList()

        ll.append(10)
        ll.append(20)
        ll.append(30)

        self.assertTrue(ll.remove_at(2))

        self.assertEqual(ll.get(0), 10)
        self.assertEqual(ll.get(1), 20)


    def test_remove_at_invalid_index(self):
        ll = LinkedList()

        ll.append(10)
        ll.append(20)

        self.assertFalse(ll.remove_at(10))
        self.assertEqual(ll.size(), 2)


    def test_remove_at_negative_index(self):
        ll = LinkedList()

        ll.append(10)
        ll.append(20)

        self.assertFalse(ll.remove_at(-1))
        self.assertEqual(ll.size(), 2)


    def test_remove_at_only_node(self):
        ll = LinkedList()

        ll.append(10)

        self.assertTrue(ll.remove_at(0))

        self.assertTrue(ll.is_empty())


    # =========================
    # Search
    # =========================

    def test_search_existing_value(self):
        ll = LinkedList()

        ll.append(10)
        ll.append(20)
        ll.append(30)

        self.assertTrue(ll.search(10))
        self.assertTrue(ll.search(20))
        self.assertTrue(ll.search(30))


    def test_search_missing_value(self):
        ll = LinkedList()

        ll.append(10)
        ll.append(20)

        self.assertFalse(ll.search(30))


    def test_search_empty_list(self):
        ll = LinkedList()

        self.assertFalse(ll.search(10))


    # =========================
    # Get
    # =========================

    def test_get_valid_indexes(self):
        ll = LinkedList()

        ll.append(10)
        ll.append(20)
        ll.append(30)

        self.assertEqual(ll.get(0), 10)
        self.assertEqual(ll.get(1), 20)
        self.assertEqual(ll.get(2), 30)


    def test_get_invalid_index(self):
        ll = LinkedList()

        ll.append(10)
        ll.append(20)

        self.assertIsNone(ll.get(2))
        self.assertIsNone(ll.get(100))


    def test_get_negative_index(self):
        ll = LinkedList()

        ll.append(10)
        ll.append(20)

        self.assertIsNone(ll.get(-1))


    def test_get_from_empty_list(self):
        ll = LinkedList()

        self.assertIsNone(ll.get(0))


    # =========================
    # Size
    # =========================

    def test_size_empty(self):
        ll = LinkedList()

        self.assertEqual(ll.size(), 0)


    def test_size_after_operations(self):
        ll = LinkedList()

        ll.append(10)
        self.assertEqual(ll.size(), 1)

        ll.append(20)
        self.assertEqual(ll.size(), 2)

        ll.prepend(5)
        self.assertEqual(ll.size(), 3)

        ll.remove(10)
        self.assertEqual(ll.size(), 2)

        ll.remove_at(0)
        self.assertEqual(ll.size(), 1)


    # =========================
    # Is Empty
    # =========================

    def test_is_empty(self):
        ll = LinkedList()

        self.assertTrue(ll.is_empty())

        ll.append(10)

        self.assertFalse(ll.is_empty())

        ll.remove(10)

        self.assertTrue(ll.is_empty())


    # =========================
    # Reverse
    # =========================

    def test_reverse_empty_list(self):
        ll = LinkedList()

        ll.reverse()

        self.assertTrue(ll.is_empty())


    def test_reverse_single_node(self):
        ll = LinkedList()

        ll.append(10)

        ll.reverse()

        self.assertEqual(ll.get(0), 10)


    def test_reverse_multiple_nodes(self):
        ll = LinkedList()

        ll.append(10)
        ll.append(20)
        ll.append(30)

        ll.reverse()

        self.assertEqual(ll.get(0), 30)
        self.assertEqual(ll.get(1), 20)
        self.assertEqual(ll.get(2), 10)


    def test_reverse_twice(self):
        ll = LinkedList()

        ll.append(10)
        ll.append(20)
        ll.append(30)

        ll.reverse()
        ll.reverse()

        self.assertEqual(ll.get(0), 10)
        self.assertEqual(ll.get(1), 20)
        self.assertEqual(ll.get(2), 30)


    # =========================
    # Combined Operations
    # =========================

    def test_combined_operations(self):
        ll = LinkedList()

        ll.append(10)
        ll.append(20)
        ll.append(30)

        ll.prepend(5)
        ll.insert(2, 15)
        ll.remove(20)
        ll.remove_at(0)
        ll.reverse()

        self.assertEqual(ll.get(0), 30)
        self.assertEqual(ll.get(1), 15)
        self.assertEqual(ll.get(2), 10)
        self.assertEqual(ll.size(), 3)


if __name__ == "__main__":
    unittest.main()
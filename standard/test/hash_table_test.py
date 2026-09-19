import unittest
from standard.hash_table_with_chaining import HashTable


class HashTableTest(unittest.TestCase):

    def test_initialization(self):
        ht = HashTable(5)

        self.assertEqual(ht.bucketSize, 5)
        self.assertEqual(ht.hashTable, [[], [], [], [], []])

    def test_hash(self):
        ht = HashTable(5)

        self.assertEqual(ht._hash(10), 0)
        self.assertEqual(ht._hash(7), 2)
        self.assertEqual(ht._hash(12), 2)

    def test_put(self):
        ht = HashTable(5)

        ht.put(10)
        ht.put(7)
        ht.put(12)

        self.assertEqual(
            ht.hashTable,
            [[10], [], [7, 12], [], []]
        )

    def test_put_collision(self):
        ht = HashTable(5)

        ht.put(10)
        ht.put(15)
        ht.put(20)

        self.assertEqual(
            ht.hashTable,
            [[10, 15, 20], [], [], [], []]
        )

    def test_put_multiple_buckets(self):
        ht = HashTable(5)

        ht.put(10)
        ht.put(7)
        ht.put(12)
        ht.put(3)

        self.assertEqual(
            ht.hashTable,
            [[10], [], [7, 12], [3], []]
        )

    def test_remove_existing_key(self):
        ht = HashTable(5)

        ht.put(10)
        ht.put(15)
        ht.put(7)

        ht.remove(15)

        self.assertEqual(
            ht.hashTable,
            [[10], [], [7], [], []]
        )

    def test_remove_head_of_bucket(self):
        ht = HashTable(5)

        ht.put(10)
        ht.put(15)
        ht.put(20)

        ht.remove(10)

        self.assertEqual(
            ht.hashTable,
            [[15, 20], [], [], [], []]
        )

    def test_remove_tail_of_bucket(self):
        ht = HashTable(5)

        ht.put(10)
        ht.put(15)
        ht.put(20)

        ht.remove(20)

        self.assertEqual(
            ht.hashTable,
            [[10, 15], [], [], [], []]
        )

    def test_remove_missing_key(self):
        ht = HashTable(5)

        ht.put(10)
        ht.put(7)

        ht.remove(100)

        self.assertEqual(
            ht.hashTable,
            [[10], [], [7], [], []]
        )

    def test_remove_from_empty_table(self):
        ht = HashTable(5)

        ht.remove(10)

        self.assertEqual(
            ht.hashTable,
            [[], [], [], [], []]
        )

    def test_duplicate_keys(self):
        ht = HashTable(5)

        ht.put(10)
        ht.put(10)

        self.assertEqual(
            ht.hashTable,
            [[10, 10], [], [], [], []]
        )

        ht.remove(10)

        self.assertEqual(
            ht.hashTable,
            [[10], [], [], [], []]
        )


if __name__ == "__main__":
    unittest.main()
import unittest

from dsa.hashtable import HashTable

class TestHashTable(unittest.TestCase):
    def test_create(self):
        ht = HashTable()
        self.assertEqual(ht.count, 0)

# get, delete, set, add
    def test_insert(self):
        ht = HashTable(1)

        self.assertEqual(ht.count, 0)
        ht.set("A", 1)
        ht.set("B", 2)
        ht.set("C", 3)
        ht.set("A", 4)
        self.assertEqual(ht.get("A"), 4)
        self.assertEqual(ht.get("B"), 2)
        self.assertEqual(ht.get("C"), 3)
        self.assertEqual(ht.count, 3)

        ht.delete("A")
        ht.delete("D")
        self.assertEqual(ht.count, 2)

        ht.delete("B")
        ht.delete("C")
        ht.delete("X")
        self.assertEqual(ht.count, 0)
        ht.set("C", 30)
        ht.set("C", 43)
        self.assertEqual(ht.count, 1)
        self.assertEqual(ht.get("A"), None)
        self.assertEqual(ht.get("C"), 43)
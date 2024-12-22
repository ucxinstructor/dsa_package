import unittest

from dsa.trie import Trie

class TestTrie(unittest.TestCase):
    def test_all(self):
        t = Trie()

        t.insert("python")
        t.insert("python")
        t.insert("pygame")
        t.insert("pandas")
        t.insert("apple")

        self.assertTrue(t.search("python"))
        self.assertTrue(t.search("pygame"))
        self.assertTrue(t.search("apple"))
        self.assertFalse(t.search("py"))
        self.assertIsNotNone(t.search_node("python"))
        self.assertIsNotNone(t.search_node("py"))
        self.assertIsNone(t.search_node("java"))
        t.delete("python")
        self.assertFalse(t.search("python"))
        self.assertIsNone(t.search_node("python"))

        # autocomplete
        words = t.autocomplete("a")
        self.assertEqual(len(words), 1)
        words = t.autocomplete("apple")
        self.assertEqual(len(words), 1)
        words = t.autocomplete("Apple")
        self.assertIsNone(words, 0)

        words = t.autocomplete("p")
        self.assertEqual(len(words), 2)
        words = t.autocomplete("py")
        self.assertEqual(len(words), 1)
        t.insert("python")
        words = t.autocomplete("py")
        self.assertEqual(len(words), 2)

        # suggest
        words = t.suggest("abc")
        self.assertEqual(words[0], "apple")

        words = t.suggest("p")
        self.assertEqual(len(words), 3)

        words = t.suggest("paper")
        self.assertEqual(words[0], "pandas")

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

    def setUp(self):
        self.trie = Trie()
        self.trie.insert("hello")
        self.trie.insert("hell")
        self.trie.insert("heaven")
        self.trie.insert("goodbye")

    def test_search_existing_word(self):
        self.assertTrue(self.trie.search("hello"))
        self.assertTrue(self.trie.search("hell"))
        self.assertTrue(self.trie.search("heaven"))
        self.assertTrue(self.trie.search("goodbye"))

    def test_search_non_existing_word(self):
        self.assertFalse(self.trie.search("world"))
        self.assertFalse(self.trie.search("helloo"))
        self.assertFalse(self.trie.search("heavens"))
        self.assertFalse(self.trie.search("goodby"))

    def test_search_empty_string(self):
        self.assertFalse(self.trie.search(""))

    def test_search_partial_word(self):
        self.assertFalse(self.trie.search("he"))
        self.assertFalse(self.trie.search("goo"))

    def test_search_node_existing_word(self):
        self.assertIsNotNone(self.trie.search_node("hello"))
        self.assertIsNotNone(self.trie.search_node("hell"))
        self.assertIsNotNone(self.trie.search_node("heaven"))
        self.assertIsNotNone(self.trie.search_node("goodbye"))

    def test_search_node_non_existing_word(self):
        self.assertIsNone(self.trie.search_node("world"))
        self.assertIsNone(self.trie.search_node("helloo"))
        self.assertIsNone(self.trie.search_node("heavens"))

    def test_delete_existing_word(self):
        self.trie.insert("test")
        self.assertTrue(self.trie.search("test"))
        self.trie.delete("test")
        self.assertFalse(self.trie.search("test"))
        self.assertIsNone(self.trie.search_node("test"))

    def test_delete_non_existing_word(self):
        self.assertFalse(self.trie.delete("nonexistent"))

    def test_delete_partial_word(self):
        self.trie.insert("testing")
        self.assertTrue(self.trie.search("testing"))
        self.trie.delete("test")
        self.assertTrue(self.trie.search("testing"))
        self.assertFalse(self.trie.search("test"))

    def test_delete_word_with_common_prefix(self):
        self.trie.insert("test")
        self.trie.insert("testing")
        self.assertTrue(self.trie.search("test"))
        self.assertTrue(self.trie.search("testing"))
        self.trie.delete("test")
        self.assertFalse(self.trie.search("test"))
        self.assertTrue(self.trie.search("testing"))

    def test_delete_empty_string(self):
        # perhaps this should be false?
        self.assertTrue(self.trie.delete(""))

    def test_search_node_empty_string(self):
        self.assertIsNone(self.trie.search_node(""))

    def test_search_node_partial_word(self):
        self.assertIsNotNone(self.trie.search_node("he"))
        self.assertIsNotNone(self.trie.search_node("goo"))

    def test_autocomplete(self):
        self.trie.insert("test")
        self.trie.insert("testing")
        self.trie.insert("tester")
        self.trie.insert("team")
        self.trie.insert("teach")

        # Test autocomplete with full word
        words = self.trie.autocomplete("test")
        self.assertEqual(sorted(words), ["test", "tester", "testing"])

        # Test autocomplete with prefix
        words = self.trie.autocomplete("te")
        self.assertEqual(sorted(words), ["teach", "team", "test", "tester", "testing"])

        # Test autocomplete with single character prefix
        words = self.trie.autocomplete("t")
        self.assertEqual(sorted(words), ["teach", "team", "test", "tester", "testing"])

        # Test autocomplete with no matching prefix
        words = self.trie.autocomplete("toast")
        self.assertIsNone(words)

        # Test autocomplete with empty string
        words = self.trie.autocomplete("")
        self.assertIsNone(words)
#        self.assertEqual(sorted(words), ["goodbye", "heaven", "hell", "hello"])

    def test_suggest(self):
        self.trie.insert("test")
        self.trie.insert("testing")
        self.trie.insert("tester")
        self.trie.insert("team")
        self.trie.insert("teach")

        # Test suggest with exact match
        words = self.trie.suggest("test")
        self.assertEqual(sorted(words), ["test", "tester", "testing"])

        # Test suggest with prefix match
        words = self.trie.suggest("te")
        self.assertEqual(sorted(words), ["teach", "team", "test", "tester", "testing"])

        # Test suggest with single character prefix
        words = self.trie.suggest("t")
        self.assertEqual(sorted(words), ["teach", "team", "test", "tester", "testing"])

        # Test suggest with no matching prefix
        words = self.trie.suggest("toast")
        self.assertEqual(sorted(words), ["teach", "team", "test", "tester", "testing"])

        # Test suggest with empty string
        words = self.trie.suggest("")
        self.assertIsNone(words)

        # Test suggest with non-existent prefix
        words = self.trie.suggest("xyz")
        self.assertIsNone(words)

    def test_copy(self):
        # Insert words into the trie
        self.trie.insert("test")
        self.trie.insert("testing")
        self.trie.insert("tester")
        self.trie.insert("team")
        self.trie.insert("teach")

        # Create a copy of the trie
        copied_trie = self.trie.copy()

        # Check that the copied trie contains the same words
        self.assertTrue(copied_trie.search("test"))
        self.assertTrue(copied_trie.search("testing"))
        self.assertTrue(copied_trie.search("tester"))
        self.assertTrue(copied_trie.search("team"))
        self.assertTrue(copied_trie.search("teach"))

        # Check that modifying the original trie does not affect the copied trie
        self.trie.delete("test")
        self.assertFalse(self.trie.search("test"))
        self.assertTrue(copied_trie.search("test"))

        # Check that modifying the copied trie does not affect the original trie
        copied_trie.delete("testing")
        self.assertFalse(copied_trie.search("testing"))
        self.assertTrue(self.trie.search("testing"))

    def test_eq(self):
        t1 = Trie()
        t2 = Trie()
        t3 = Trie()
        for word in ["apple", "banana", "cat"]:
            t1.insert(word)
            t2.insert(word)
        for word in ["apple", "banana"]:
            t3.insert(word)
        self.assertEqual(t1, t2)
        self.assertNotEqual(t1, t3)

        self.assertNotEqual(t1, ["apple", "banana", "cat"])


if __name__ == '__main__':
    unittest.main()
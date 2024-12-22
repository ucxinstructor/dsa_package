""" Module containing trie class. """

class TrieNode:
    """ 
    A trie node implementation.
    """
    def __init__(self):
        #: a dictionary of key (character) ->value (references)
        self.children = {}

class Trie:
    """ 
    A trie implementation. 
    """
    #: end marker
    end_marker = "*"

    def __init__(self):
        """ 
        Initialize a trie.
        """        
        #: root of the trie
        self.root = TrieNode()
            
    def insert(self, word: str):
        """ 
        Insert a word into a trie.
        
        Args:
            word: word to insert into a trie
        """        
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()

            current = current.children[c]
        current.children[Trie.end_marker] = None
        current.is_end = True
    
    def search(self, word: str):
        """ 
        Search for a substring in a trie.
        
        Args:
            word: word to search for
        
        Returns:
        True if the complete word is found
        """        
        if len(word) == 0:
            return False

        current = self.root
        for c in word + Trie.end_marker:
            if c not in current.children:
                return False
            current = current.children[c]
        return True

    def search_node(self, word: str):
        """ 
        Search for a substring in a trie.
        
        Args:
            word: word to search for
        
        Returns:
        TriedNode where the string begins
        None if the word is not found
        """        
        if len(word) == 0:
            return None

        current = self.root
        for c in word:
            if c not in current.children:
                return None
            current = current.children[c]
        return current
    
    def delete(self, word: str, i=0, current=None):
        """ 
        Delete a word from the trie.
        
        Args:
            word: word to delete
            i: index of character
            current: current node

        Returns:
        Boolean indicating if child node can be deleted
        """        
        if i == len(word):
            return True

        # set up the beginning of delete
        if current is None:
            current = self.root
            word = word + Trie.end_marker

        char = word[i]

        # character is not found, so word is invalid and return False
        if char not in current.children:
            return False
        
        next_node = current.children[char]
        should_delete_ref = self.delete(word, i + 1, next_node)

        # delete the child reference
        if should_delete_ref:
            del current.children[char]

            # return True if there are no more children
            return len(current.children) == 0
        return False
    
    def delete_preorder(self, word, i=0, current=None):
        """ 
        Delete a word using preorder (Do not use! For demonstration purposes only).
        
        Args:
            word: word to delete
            i: index of character
            current: current node

        Returns:
        Boolean indicating if child node can be deleted
        """        
        if i == len(word):
            return True

        if current is None:
            current = self.root
            word = word + Trie.end_marker

        char = word[i]
        if char not in current.children:
            return False
        
        next_node = current.children[char]

        del current.children[char]

        self.delete(word, i + 1, next_node)
        
        return False
            
    def list_words(self, node=None, word: str = "", words=None):
        """ 
        Return a list of words.
        
        Args:
            node: current trie node
            word: word to build after each recursive call
            words: list of words

        Returns:
        List of words that begin with a given prefix.
        """        
        if words is None:
            words = []

        current = node
        if node is None:
            current = self.root
        
        for key, node in sorted(current.children.items()):
            if key == Trie.end_marker:
                words.append(word)
            else:
                self.list_words(node, word + key, words)
        return words
    
    def autocomplete(self, prefix: str):
        """ 
        Return a list of words that begin with a given prefix.
        
        Args:
            prefix: prefix to search for

        Returns:
        List of words that begin with a given prefix.
        None if there are no matching words.
        """        
        current = self.search_node(prefix)
        if current is None:
            return None
        return self.list_words(current, prefix)
    
    def suggest(self, prefix: str):
        """ 
        Return a list of close words with a given prefix.
        
        Args:
            prefix: prefix to search for

        Returns:
        List of words that are similar to a given prefix.
        None if there are no matching words.
        """        
        if prefix is None or len(prefix) == 0:
            return None
        suggestions = self.autocomplete(prefix)
        if suggestions is None or len(suggestions) == 0:
            return self.suggest(prefix[:-1])
        else:
            return suggestions
    
    def copy_node(self, node):
        """
        Recursively deep copy a node and its children.
        """
        if not node:
            return
        new_node = TrieNode()
        for char, child in node.children.items():
            new_node.children[char] = self._deep_copy_node(child)
        return new_node

    def copy(self):
        """
        Create a deep copy of the Trie.
        """
        new_trie = Trie()
        new_trie.root = self.copy_node(self.root)
        return new_trie

Trie Quick Start
================

Description
-----------

A trie (prefix tree) is a tree-based data structure optimized for storing and querying strings, especially for operations based on prefixes.

Creation
--------

**Import class**

.. code-block:: python

	from dsa.trie import Trie

**Creation**

Create an empty trie:

.. code-block:: python

	t = Trie()

Common Operations
-----------------

**Insert**

Insert a word into a trie.

.. code-block:: python

	t.insert("apple")
	t.insert("app")

**Search**

Search for a word in a trie.

.. code-block:: python

	t.search("apple")   # True
	t.search("appl")    # False (missing end marker)

**Search node**

Search for a substring in a trie.

.. code-block:: python

	node = t.search_node("app")
	node is not None      # True if prefix exists

**Delete**

Delete a word from the trie.

.. code-block:: python

	t.delete("apple")
	t.search("apple")   # False

**Delete (preorder)**

Delete a word using preorder (Do not use! For demonstration purposes only).

.. code-block:: python

	# Not recommended, shown for completeness
	t.delete_preorder("app")

**List words**

Return a list of all words in the trie.

.. code-block:: python

	words = t.list_words()   # e.g., ["app"] after deletions above

**Build word list**

Helper method to return a list of words given a starting node.

.. code-block:: python

	node = t.search_node("ap")
	words = t.build_word_list(node, "ap")

**Prefix**

Return a list of words that begin with a given prefix.

.. code-block:: python

	t.insert("bat")
	t.insert("batch")
	t.prefix("ba")        # ["bat", "batch"]

**Suggest**

Return a list of close words with a given prefix.

.. code-block:: python

	t.suggest("batc")     # Falls back to "bat" prefix → ["batch"]


**Printing Contents**

Use the TrieDraw class to draw a visual representation of a trie.

.. code-block:: python

   from dsa.draw import TrieDraw

   t = Trie()
   t.insert("cab")
   t.insert("car")
   t.insert("cut")
   
   td = TrieDraw(t)
   td.draw()

.. figure:: images/trie.png
   :alt: Trie structure image
   :width: 400px

   Example of a Trie structure using TrieDraw.

Copy & Equality
---------------

**Copy**

Create a deep copy of the Trie.

.. code-block:: python

	t2 = t.copy()

**Equality**

Compare two Trie objects for value-based equality (all words in the trie).

.. code-block:: python

	t3 = Trie()
	for w in t.list_words():
		 t3.insert(w)
	t == t3    # True if same words

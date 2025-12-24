HashTable Quick Start
===================

Description
-----------

A hashtable is a data structure that implements an associative array, using a hash function to map keys to values for efficient lookups.

Creation
--------

**Import class**

.. code-block:: python

   from dsa.hashtable import HashTable  # or the appropriate HashTable class

**Creation**

Create a hashtable with default capacity of 20:

.. code-block:: python

   ht = HashTable()

Create a hashtable with a capacity of 100:

.. code-block:: python

   ht = HashTable(100)

Common Operations
-----------------

**Set**

Set a key-value pair in the hashtable. If key exists, replace the value otherwise, create a new key-pair.

.. code-block:: python

   ht.set('key', 'value')  # Set key-value pair

**Get**

Get corresponding value of a given key in the hash table.

.. code-block:: python

   value = ht.get('key')  # Get value for key

**Remove**

Remove key-value pair if specified key is found. Raise KeyError if not found.

.. code-block:: python

   ht.remove('key')  # Remove key-value pair


**Printing Contents**

Use print() to print the contents of the set.

.. code-block:: python

   ht = HashTable()
   ht.set(1, "a")
   ht.set(2, "b")
   ht.set(3, "c")
   ht.set(1, "d")

   print(ht)

Outputs the following:

.. code-block:: python

   {1:d, 2:b, 3:c}


Other Related Classes
---------------------

- :class:`dsa.hashset.HashSet`
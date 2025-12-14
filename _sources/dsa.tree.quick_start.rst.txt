Tree Quick Start
==============

Description
-----------

A binary search tree is a data structure that maintains sorted order, allowing efficient search, insertion, and deletion operations.

Creation
--------

**Import class**

.. code-block:: python

   from dsa.tree import Tree  # or the appropriate Tree class

**Creation**

Create an empty binary search tree:

.. code-block:: python

   t = Tree()

Common Operations
-----------------

**Insert**

Insert a value in the binary search tree.

.. code-block:: python

   t.insert(10)  # Insert 10 into the tree

**Search**

Search for a value in the binary search tree.

.. code-block:: python

   node = t.search(10)  # Search for 10

**Delete**

Delete a value from the binary search tree.

.. code-block:: python

   t.delete(10)  # Delete 10 from the tree

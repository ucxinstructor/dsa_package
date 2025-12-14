Tree Quick Start
==============

Description
-----------

A binary search tree is a data structure that maintains sorted order, allowing efficient search, insertion, and deletion operations.

Creation
--------

**Import class**

.. code-block:: python

   from dsa.tree import Tree, TreeNode  # or the appropriate Tree class

**Creation**

Create an empty binary search tree:

.. code-block:: python

   t = Tree()

TreeNodes Construction
---------------------------

**Build a binary search tree using TreeNodes**

.. code-block:: python

   # Create TreeNode instances
   root = TreeNode(10)
   root.left = TreeNode(5)
   root.right = TreeNode(15)
   root.left.left = TreeNode(3)
   root.right.right = TreeNode(20)

   # Initialize the Tree with the root
   t = Tree(root=root)
This creates the following tree structure:

.. code-block::

       10
      /  \
     5    15
    /      \
   3        20

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

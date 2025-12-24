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
   
   
**Printing Contents**

Use print method to print the elements of the tree.

.. code-block:: python

   t = Tree()
   t.insert(20)
   t.insert(10)
   t.insert(30)
   
   t.print()

Outputs the following (note that the output is rotated 90 degrees to the left):

.. code-block:: python

     30
  20
     10
     
Alternative way to print the tree:

.. code-block:: python
   
   from dsa.pretty_print import tree_print
   tree_print(t)

Outputs the following:

.. code-block:: python   

    20
  10 30


Use the TreeDraw class to draw a visual representation of a tree.

.. code-block:: python   

   from dsa.draw import TreeDraw
   t = Tree()
   t.insert(20)
   t.insert(10)
   t.insert(30)

   td = TreeDraw(t)
   td.draw()

.. figure:: images/tree.png
   :alt: Tree structure image
   :width: 400px

   Example of a Tree structure using TreeDraw.
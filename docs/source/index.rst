UCXDSA Package
=============================================================

A collection of data structures and algorithms implemented in Pythonfor use in UC Berkeley Extension's 
Computer Science X404.1: Data Structures and Algorithms Class.


Overview
--------

This package is an educational tool for students to learn and experiment with data structures and algorithms. It helps learners understand core concepts and allows developers to explore implementations.

Written in Python, the package emphasizes readability and clarity over performance or optimization.
**Not intended for production use.**

Project repository: `UCXDSA on GitHub <https://github.com/ucxinstructor/dsa_package>`_

Command Line Installation
-------------------------

.. code-block:: bash

   pip install ucxdsa

Updating an Existing Version
-----------------------------------------------

.. code-block:: bash

   pip install --upgrade ucxdsa

Determining Current Version
-----------------------------------------------
To determine the dsa package version, enter the following in Python or Jupyter:

.. code-block:: python

   import dsa
   print(dsa.version)

or from the terminal

.. code-block:: bash

   pip show ucxdsa

Quick Usage Guide
-----------------

.. code-block:: python

   from dsa.modulename import classname

Replace ``modulename`` and ``classname`` with the module and class to be used.



Contributing
------------

We welcome contributions! You can help by:

- Reporting bugs or unexpected behavior
- Suggesting new features or improvements
- Submitting pull requests with code enhancements or documentation updates

How to Contribute
-----------------

1. Fork the repository.
2. Create a new branch for your changes.
3. Commit your changes with clear messages.
4. Submit a pull request explaining your changes.

Reporting Issues
----------------

Please use the  `GitHub Issues page <https://github.com/ucxinstructor/dsa_package/issues>`_  to report any problems or request features. Provide detailed information so we can reproduce and address the issue efficiently.

Thank you for helping improve this project!


.. toctree::
   :maxdepth: 2
   :caption: Contents:
   :hidden:

   Home <self>
   TODO

.. toctree::
   :maxdepth: 2
   :caption: Quick Start Guides
   :hidden:

   dsa.array.quick_start
   dsa.stack.quick_start
   dsa.queue.quick_start
   dsa.deque.quick_start
   dsa.linkedlist.quick_start
   dsa.hashset.quick_start
   dsa.hashtable.quick_start
   dsa.tree.quick_start
   dsa.heap.quick_start
   dsa.trie.quick_start
   dsa.graph.quick_start
   dsa.draw.quick_start
      
.. toctree::
   :maxdepth: 2
   :caption: Core Data Structures
   :hidden:

   modules
       
.. toctree::
   :maxdepth: 2
   :caption: Linear Structures
   :hidden:
   
   Array Module <dsa.array>
   Stack Module <dsa.stack>
   Queue Module <dsa.queue>
   Deque Module <dsa.deque>

.. toctree::
   :maxdepth: 2
   :caption: Linked List
   :hidden:

   Singly Linked List Module <dsa.singlylinkedlist>
   Doubly Linked List Module <dsa.doublylinkedlist>

.. toctree::
   :maxdepth: 2
   :caption: Hash
   :hidden:

   HashSet Module <dsa.hashset>
   HashTable Module <dsa.hashtable>

.. toctree::
   :maxdepth: 2
   :caption: Tree
   :hidden:

   Tree Module <dsa.tree>
   Heap Module <dsa.heap>
   Trie Module <dsa.trie>

.. toctree::
   :maxdepth: 2
   :caption: Graph
   :hidden:

   Graph Module <dsa.graph>

.. toctree::
   :maxdepth: 2
   :caption: Algorithms
   :hidden:

   Graph Module <dsa.graph_traversal>
   Dijkstra Module <dsa.dijkstra>
   Prim Module <dsa.prim>
   Huffman Module <dsa.huffman>

.. toctree::
   :maxdepth: 2
   :caption: Helper Modules
   :hidden:

   Draw Module <dsa.draw>
   Pretty Print Module <dsa.pretty_print>
   Sort Tools Module <dsa.sorttools>
   Generator Module <dsa.generators>

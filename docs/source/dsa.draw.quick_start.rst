Draw Quick Start
================

Description
-----------

Draw graphic representations  of the following data structures.
- Tree
- Trie
- Heap
- Graph

To visualize any class, follow these steps:
	1.	Import the Draw class for the data structure.
	2.	Create an instance of the data structure.
	3.	Initialize the Draw class with the data structure as the argument.
	4.	Call the draw() method of the Draw object.
	


Import Class
--------------

**Import class**

Import the class related to the data structure to be visualized.

.. code-block:: python

  from dsa.draw import TreeDraw
  from dsa.draw import HeapDraw
  from dsa.draw import TrieDraw
  from dsa.draw import GraphDraw

**Creation**

Initialize the Draw class with the data structure as the argument.

.. code-block:: python

   # create Tree
   t = Tree()
   td = TreeDraw(t)
   
   # create Heap
   h = Heap()
   hd = HeapDraw(h)

   # create Trie
   trie = Trie()
   trd = TreeDraw(trie)

   # create Graph
   g = Graph()
   gd = GraphDraw(g)
   


Draw the object by invoking the draw() method

.. code-block:: python

    td.draw()
    hd.draw()
    trd.draw()
    gd.draw()
    

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
   

Use the HeapDraw class to draw a visual representation of a heap.

.. code-block:: python   

   from dsa.draw import HeapDraw
   h = Heap()
   h.insert(1)
   h.insert(2)
   h.insert(3)
   h.insert(4)
 
   hd = HeapDraw(h)
   hd.draw()

.. figure:: images/heap.png
   :alt: Heap structure image
   :width: 400px

   Example of a Heap structure using HeapDraw.


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



Use the GraphDraw class to draw a visual representation of a graph.

.. code-block:: python

   from dsa.draw import GraphDraw

   g = Graph.create_adjacency_matrix(directed=True, weighted=True)

   g.add_edge("A", "B", 1)
   g.add_edge("A", "C", 2)
   g.add_edge("B", "C", 3)
   
   # accepts any graph type
   gd = GraphDraw(g)
   gd.draw()

.. figure:: images/graph.png
   :alt: Graph structure image
   :width: 400px

   Example of a Graph structure using GraphDraw.

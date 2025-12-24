Graph Quick Start
=================

Description
-----------

Creation
--------

**Import class**

To use Graphs, first import the Graph class from the graph module

.. code-block:: python

  from dsa.graph import Graph

**Creation**
Create a Graph

Before creating a graph, choose its characteristics:

- Representation: adjacency matrix or adjacency list
- Edge direction: directed or undirected
- Weights: weighted or unweighted


Create an adjacency matrix graph with undirected and unweighted edges (default):

.. code-block:: python

   g = Graph.create_adjacency_matrix()


Create an adjacency list graph with undirected and unweighted edges:

.. code-block:: python

   g = Graph.create_adjacency_list(directed=False, weighted=False)

Create an adjacency list graph with directed and weighted edges:

.. code-block:: python

   g = Graph.create_adjacency_list(directed=True, weighted=True)

Common Operations
-----------------

Add a vertex to a graph:

.. code-block:: python

   g = Graph.create_adjacency_list(directed=True, weighted=True)
   g.add_vertex("A")
   g.add_vertex("B")
   g.add_vertex("C")

Add an edge to a graph:

.. code-block:: python

   g.add_edge("A", "B", 1) #   omit weight for non-weighted graphs: g.add_edge("A", "B")
   g.add_edge("A", "C", 2)
   g.add_edge("B", "C", 3)


Existence Methods
    - Vertex existence
    - Edge existence

.. code-block:: python

  from dsa.graph import Graph

  g = Graph.create_adjacency_matrix(directed=True, weighted=True)
  g.add_vertex("A")
  g.add_vertex("B")
  g.add_vertex("C")
  
  g.add_edge("A", "B", 1)
  g.add_edge("A", "C", 2)
  g.add_edge("B", "C", 3)

  g.has_vertex("A") # True
  g.has_vertex("B") # True
  g.has_vertex("D") # False

  g.has_edge("A", "B") # True
  g.has_edge("A", "C") # True
  g.has_edge("C", "B") # False

List Methods
    - List of vertices
    - List of edges
    - List of adjacents from a given edge

To list all of the vertices in a graph:

.. code-block:: python

  g.vertices()

Output:

.. code-block:: python

  ['A', 'B', 'C']
  

To list all of the edges in a graph:

.. code-block:: python

  g.edges()


Output (starting vertex, ending vertex and weight (if weighted graph) as a list of tuples):

.. code-block:: python

  [('A', 'B', 1), ('A', 'C', 2), ('B', 'C', 3)]


To list all of the adjacents from a given edge in a graph:

.. code-block:: python

  g.adjacents("A")
  
Output:

.. code-block:: python

  ['B', 'C']


To list all of the adjacents from a given edge in a graph:

.. code-block:: python

  g.adjacent_items("A")
  
Output as a list of tuples (includes weight in a weighted graph):

.. code-block:: python

  [('B', 1), ('C', 2)]

View contents

To list the contents of an adjacency matrix graph:

.. code-block:: python

  g.print_matrix()
  
Output:

.. code-block:: python

     |  A   B   C 
  ----------------
   A |      1   2 
   B |          3 
   C |            
   
   
   
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

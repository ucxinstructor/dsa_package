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

- Add Vertices and Edges
  - add_vertex(v)
  - add_edge(u, v, weight=None)
- Query
  - has_edge(u, v)
  - has_vertex(v)


Other Related Classes
---------------------


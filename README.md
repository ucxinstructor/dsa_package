# UC Berkeley Extension - Data Structures and Algorithms Class 

A collection of classes and functions for use in Comp Sci X404.1: Data Structures and Algorithms Class.

[API Documentation](src/html/dsa)	
## 2024.12.22
* Created Github Pages access to documentation
* Added more details to documentation

## 2024.08.16.1
Fixed versioning issue. Can now determine version by typing:
```
import dsa
dsa.version
```
or

```
dsa.__version__
```
## 2024.08.16
moved Trie end_marker from an instance variable to a class variable (Trie.end_marker)

## 2024.08.15
### dsa.draw
* new module to provide optional NetworkX graphics to:
* graphs
* tries
* trees
* heaps

### dsa module
ran code through RUFF

### dsa.graphs module
* Added vertices() method to AdjacencyListGraph, AdjacencyListWeightedGraph
* Dropped Vertex classes

### dsa.tree
renamed Node class to TreeNode

## 2024.7.23
### dsa.graphs module
* added is_edge() methods for AdjacencyMatrixGraph, AdjacencyMatrixWeightedGraph, AdjacencyListGraph, AdjacencyListWeightedGraph
* added index operator (returns a list of adjacent labels) for AdjacencyMatrixGraph, AdjacencyMatrixWeightedGraph
* cleaned up and refactored parameter names

## 2024.7.19
### dsa.graphs module
* Added AdjacencyMatrixGraph, AdjacencyMatrixWeightedGraph, AdjacencyListGraph, AdjacencyListWeightedGraph
* Deprecated: Vertex, WeightedVertex

#### dsa.heap module
* Removed MinHeap option from the Heap class
* Added dedicated MinHeap class
* Added Priority Queue class

### dsa package
Misc. code improvements, documentation updates and API consistency

# TODO
* Separate the Dijkstra code from graph
* Add Prim's algorithm
* General: Add more type hints

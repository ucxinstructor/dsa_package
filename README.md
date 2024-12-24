# UC Berkeley Extension - Data Structures and Algorithms Class 

A collection of classes and functions for use in UC Berkeley Extension's Comp Sci X404.1: Data Structures and Algorithms Class.

[API Documentation](src/html/dsa)	

Command Line Installation
```
pip install ucxdsa
```

Updating an existing version of the DSA package

```
pip install --upgrade ucxdsa
```

Quick Usage Guide

```
from dsa.modulename import classname
```

To determine the version, enter the following in Python or Jupyter:

```
import dsa
print(dsa.version)
``` 
***
# Revision History
## 2024.12.24
* Made default size for Trie Graph larger
* Cleaned up Heap module
* Cleaned up Huffman module to use dsa data structures
* Added more tests
* Added more details to documentation

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
* Make an abstract Graph class

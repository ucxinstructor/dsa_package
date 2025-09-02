# UC Berkeley Extension - Data Structures and Algorithms Class 

A collection of classes and functions for use in UC Berkeley Extension's Comp Sci X404.1: Data Structures and Algorithms Class.

This package is designed as an educational tool for students to learn and experiment with data structures and algorithms.
It is written in Python with an emphasis on readability and clarity, rather than performance or optimization.
Not intended for production use.


[API Documentation](https://ucxinstructor.github.io/dsa_package/src/html/dsa/)


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
or from the terminal
```
pip show ucxdsa
```

***
# Revision History
## 2025.09.02
* Added Hash Set 
* Added equality testing for array, stack, queue, deque, linkedlist and heap classes
* Renamed Hashtable delete() to remove()
* Updated Dijkstra's algorithm implementation to follow lecture more closely

## 2025.07.17
* Added generators module -- functions to generate linear and random arrays, queues, stacks, tries, heaps, trees and graphs (warning: a work in progress)
* Hashtable updates
  * Allow non-strings for keys
  * Works with index operator [] and in operator
  * Added pop() method (thank you, Rishab!)
* Cleaned up some test cases (singly linked list, doubly linked list, stack, queue, hash table)

## 2025.07.05
* Added two new functions to sorttools: array_details() - returns the length, and the contents of an array/list  and generate_almost_sorted_array() 

## 2025.06.25
* Added boundary checking for shift_left() and shift_right() Array methods. Also, changed to accept only one argument starting argument. (Thanks for reporting this, Alejandro!)
  
## 2025.06.14
* Added iterative versions of insert and delete BST methods 

## 2025.06.11
* Revised Trie Draw to draw circles instead of squares

## 2025.06.09
* Added queue-like synonyms for deque methods

## 2025.3.22
* Added CircularArray and CircularQueue classes
* SinglyLinkedList and DoublyLinkedList classes
  * Added separate delete_head() and delete_tail() methods
  * Changed behavior insert() so if index == count, performs an append()
* Changed behavior insert() in Array class so if index == count, performs an append()
* Queue and Heap classes
  * Refactored to_list() to raw_view()
  * Added to_ordered_list() to Queue class
  * Added to_sorted_list() method to Heap class
* Updated unit tests

## 2025.2.10
* Cleaned up comments
* Renamed df_traverse() to dfs_traverse() and bf_traverse() to bfs_traverse() 

## 2025.2.9
* Refactored Dijkstra's algorithm code
* Added delete_edge() method to graphs
* Removed all duplicate add_edge() methods such as add_adjacent_vertex()
* Removed all add_directed_edge() methods and added directed argument to add_edge()
* Minor comment fixes

## 2025.1.31
* Fixed bug when DoublyLinkedList delete of the last index throws an Exception 

## 2025.1.29
* Added is_sorted() in sorttools
* Fixed a bug when displaying a TreeNode in repr() format
* Update some modules to be more pyright compliant

## 2025.1.19
* Fixed bug in Queue to_list() method (thanks, Charles!)

## 2025.1.17
* Updated hash function code

## 2025.1.15
* Cleaned up README.md

## 2024.12.24
* Made default size for Trie graph larger
* Cleaned up Heap module
* Cleaned up Huffman module to use DSA data structures
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
* Overload comparison operator for all data structures
* Make an abstract Graph class?
* Allow NetworkX access to draw class
* Allow undirected option in edges() method of the graph class
* Capture and verify output of tree structures
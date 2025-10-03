from dsa.array import Array, DynamicArray
from dsa.stack import Stack, DynamicStack
from dsa.queue import Queue, DynamicQueue
from dsa.deque import Deque

from dsa.singlylinkedlist import LinkedList
from dsa.doublylinkedlist import DoublyLinkedList

from dsa.tree import Tree, TreeNode
from dsa.heap import Heap
from dsa.trie import Trie

from dsa.graph import AdjacencyListGraph, AdjacencyListWeightedGraph
from dsa.graph import AdjacencyMatrixGraph, AdjacencyMatrixWeightedGraph

import random

def random_array(size: int, min_val: int=0, max_val=100) -> Array:
    """
    Generates a random array of integers.
    arguments:
        size -- number of elements in the array
        min_val -- minimum value of the elements
        max_val -- maximum value of the elements
    returns: 
        Array   
    """
    array = Array(capacity=size)
    for _ in range(size):
        array.append(random.randint(min_val, max_val))
    return array

def random_dynamicarray(size: int, min_val: int=0, max_val=100) -> DynamicArray:
    """
    Generates a random dynamic array of integers.
    arguments:
        size -- number of elements in the array
        min_val -- minimum value of the elements
        max_val -- maximum value of the elements
    returns: 
        DynamicArray
    """
    array = DynamicArray()
    for _ in range(size):
        array.append(random.randint(min_val, max_val))
    return array

def random_stack(size: int, min_val: int=0, max_val=100) -> Stack:
    """
    Generates a random stack of integers.
    arguments:
        size -- number of elements in the stack
        min_val -- minimum value of the elements
        max_val -- maximum value of the elements
    returns: 
        Stack
    """
    stack = Stack(capacity=size)
    for _ in range(size):
        stack.push(random.randint(min_val, max_val))
    return stack

def linear_stack(size: int, min_val: int=0, max_val=100) -> Stack:
    """
    Generates a linear stack of integers.
    arguments:
        size -- number of elements in the stack
        min_val -- minimum value of the elements
        max_val -- maximum value of the elements
    returns: 
        Stack
    """
    stack = Stack(capacity=size)
    for i in range(size):
        stack.push(i + min_val)
    return stack

def random_dynamic_stack(size: int, min_val: int=0, max_val=100) -> DynamicStack:
    """
    Generates a random dynamic stack of integers.
    arguments:
        size -- number of elements in the stack
        min_val -- minimum value of the elements
        max_val -- maximum value of the elements
    returns: 
        DynamicStack
    """
    stack = DynamicStack()
    for _ in range(size):
        stack.push(random.randint(min_val, max_val))
    return stack

def linear_dynamic_stack(size: int, min_val: int=0, max_val=100) -> DynamicStack:
    """
    Generates a linear dynamic stack of integers.
    arguments:
        size -- number of elements in the stack
        min_val -- minimum value of the elements
        max_val -- maximum value of the elements
    returns: 
        DynamicStack
    """
    stack = DynamicStack()
    for i in range(size):
        stack.push(i + min_val)
    return stack

def random_queue(size: int, min_val: int=0, max_val=100) -> Queue:
    """
    Generates a random queue of integers.
    arguments:
        size -- number of elements in the queue
        min_val -- minimum value of the elements
        max_val -- maximum value of the elements
    returns: 
        Queue
    """
    queue = Queue(capacity=size)
    for _ in range(size):
        queue.enqueue(random.randint(min_val, max_val))
    return queue


def linear_queue(size: int, min_val: int=0, max_val=100) -> Queue:
    """
    Generates a linear queue of integers.
    arguments:
        size -- number of elements in the queue
        min_val -- minimum value of the elements
        max_val -- maximum value of the elements
    returns: 
        Queue
    """
    queue = Queue(capacity=size)
    for i in range(size):
        queue.enqueue(i + min_val)
    return queue

def random_dynamic_queue(size: int, min_val: int=0, max_val=100) -> DynamicQueue:
    """
    Generates a random dynamic queue of integers.
    arguments:
        size -- number of elements in the queue
        min_val -- minimum value of the elements
        max_val -- maximum value of the elements
    returns: 
        DynamicQueue
    """
    queue = DynamicQueue()
    for _ in range(size):
        queue.enqueue(random.randint(min_val, max_val))
    return queue

def linear_dynamic_queue(size: int, min_val: int=0, max_val=100) -> DynamicQueue:
    """
    Generates a linear dynamic queue of integers.
    arguments:
        size -- number of elements in the queue
        min_val -- minimum value of the elements
        max_val -- maximum value of the elements
    returns: 
        DynamicQueue
    """
    queue = DynamicQueue()
    for i in range(size):
        queue.enqueue(i + min_val)
    return queue

def random_deque(size: int, min_val: int=0, max_val=100) -> Deque:
    """
    Generates a random deque of integers.
    arguments:
        size -- number of elements in the deque
        min_val -- minimum value of the elements
        max_val -- maximum value of the elements
    returns: 
        Deque
    """
    deque = Deque(capacity=size)
    for _ in range(size):
        if random.choice([True, False]):
            deque.append_left(random.randint(min_val, max_val))
        else:
            deque.append_right(random.randint(min_val, max_val))
    return deque

def random_linked_list(size: int, min_val: int=0, max_val=100) -> LinkedList:
    """
    Generates a random linked list of integers.
    arguments:
        size -- number of elements in the linked list
        min_val -- minimum value of the elements
        max_val -- maximum value of the elements
    returns: 
        LinkedList
    """
    linked_list = LinkedList()
    for _ in range(size):
        linked_list.append(random.randint(min_val, max_val))
    return linked_list

def linear_linked_list(size: int, min_val: int=0, max_val=100) -> LinkedList:
    """
    Generates a linear linked list of integers.
    arguments:
        size -- number of elements in the linked list
        min_val -- minimum value of the elements
        max_val -- maximum value of the elements
    returns: 
        LinkedList
    """
    linked_list = LinkedList()
    for i in range(size):
        linked_list.append(i + min_val)
    return linked_list


def random_doubly_linked_list(size: int, min_val: int=0, max_val=100) -> DoublyLinkedList:
    """
    Generates a random doubly linked list of integers.
    arguments:
        size -- number of nodes in the list
        min_val -- minimum value of the nodes
        max_val -- maximum value of the nodes
    returns: 
        DoublyLinkedList
    """
    doubly_linked_list = DoublyLinkedList()
    for _ in range(size):
        doubly_linked_list.append(random.randint(min_val, max_val))
    return doubly_linked_list

def linear_doubly_linked_list(size: int, min_val: int=0, max_val=100) -> DoublyLinkedList:
    """
    Generates a linear doubly linked list of integers.
    arguments:
        size -- number of nodes in the list
        min_val -- minimum value of the nodes       
        max_val -- maximum value of the nodes
    returns: 
        DoublyLinkedList
    """
    doubly_linked_list = DoublyLinkedList()
    for i in range(size):
        doubly_linked_list.append(i + min_val)
    return doubly_linked_list

def random_binary_tree(n: int) -> 'Tree':
    """Generates a random binary tree.
    arguments:
        n -- number of nodes in the tree
    returns: 
        Tree
    """
    tree = Tree()

    tree.root = random_binary_tree_node(n)

    return tree

def random_binary_tree_node(n: int) -> TreeNode:
    """
    Generates a random binary tree with exactly n nodes.
    arguments:
        n -- number of nodes in the tree
    returns: 
        TreeNode
    """
    if n == 0:
        return None
    root = TreeNode(random.randint(0, 100))
    n -= 1
    # Randomly decide how many nodes go to the left (0 to n)
    left_count = random.randint(0, n)
    right_count = n - left_count
    root.left = random_binary_tree_node(left_count)
    root.right = random_binary_tree_node(right_count)
    return root

def random_heap(n: int) -> Heap:
    """Generates a random heap.
    arguments:
        n -- number of nodes in the heap
    returns: 
        Heap
    """
    from dsa.heap import Heap
    heap = Heap()
    for _ in range(n):
        heap.insert(random.randint(0, 100))
    return heap

def random_trie(n: int) -> Trie:
    """Generates a random trie.
    
    arguments:
        n -- number of words in the trie
    returns: 
        Trie
    """
    from dsa.trie import Trie
    trie = Trie()
    for _ in range(n):
        word_length = random.randint(1, 10)
        word = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(word_length))
        trie.insert(word)
    return trie

# Generates a random graphs 
# options: directed, undirected, weighted, unweighted

def random_adjacency_matrix_graph(n, density=0.1, directed=False) -> AdjacencyMatrixGraph:
    # create a list of strings starting from "A" to "Z", then "AA", "AB", etc.
    labels = [chr(i) for i in range(65, 65 + n)]
    graph = AdjacencyMatrixGraph(labels=labels)
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < density:
                graph.add_edge(labels[i], labels[j], directed=directed)
    return graph

def random_adjacency_matrix_weighted_graph(n, density=0.1, directed=False) -> AdjacencyMatrixWeightedGraph:
    # create a list of strings starting from "A" to "Z", then "AA", "AB", etc.
    labels = [chr(i) for i in range(65, 65 + n)]
    graph = AdjacencyMatrixWeightedGraph(labels=labels)
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < density:
                weight = random.randint(1, 10)
                graph.add_edge(labels[i], labels[j], weight, directed=directed)
    return graph

def random_adjacency_list_graph(n, density=0.1, directed=False) -> AdjacencyListGraph:
    # create a list of strings starting from "A" to "Z", then "AA", "AB", etc.
    labels = [chr(i) for i in range(65, 65 + n)]
    graph = AdjacencyListGraph()
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < density:
                graph.add_edge(labels[i], labels[j], directed=directed)
    return graph

def random_adjacency_list_weighted_graph(n, density=0.1, directed=False) -> AdjacencyListWeightedGraph:
    # create a list of strings starting from "A" to "Z", then "AA", "AB", etc.
    labels = [chr(i) for i in range(65, 65 + n)]
    graph = AdjacencyListWeightedGraph()
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < density:
                weight = random.randint(1, 10)
                graph.add_edge(labels[i], labels[j], weight, directed=directed)
    return graph
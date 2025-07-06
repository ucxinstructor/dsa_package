from calendar import c
from dsa.array import Array, DynamicArray
from dsa.stack import Stack, DynamicStack
from dsa.queue import Queue, DynamicQueue
from dsa.deque import Deque

from dsa.singlylinkedlist import LinkedList
from dsa.doublylinkedlist import DoublyLinkedList

from dsa.tree import Tree, TreeNode
from dsa.heap import Heap
from dsa.trie import Trie

import random

def random_array(size: int, min_val: int=0, max_val=100) -> Array:
    """Generates a random array of integers."""
    array = Array(capacity=size)
    for _ in range(size):
        array.append(random.randint(min_val, max_val))
    return array

def random_dynamicarray(size: int, min_val: int=0, max_val=100) -> DynamicArray:
    """Generates a random dynamic array of integers."""
    array = DynamicArray()
    for _ in range(size):
        array.append(random.randint(min_val, max_val))
    return array

def random_stack(size: int, min_val: int=0, max_val=100) -> Stack:
    """Generates a random stack of integers."""
    stack = Stack(capacity=size)
    for _ in range(size):
        stack.push(random.randint(min_val, max_val))
    return stack

def random_dynamic_stack(size: int, min_val: int=0, max_val=100) -> DynamicStack:
    """Generates a random dynamic stack of integers."""
    stack = DynamicStack()
    for _ in range(size):
        stack.push(random.randint(min_val, max_val))
    return stack

def random_queue(size: int, min_val: int=0, max_val=100) -> Queue:
    """Generates a random queue of integers."""
    queue = Queue(capacity=size)
    for _ in range(size):
        queue.enqueue(random.randint(min_val, max_val))
    return queue


def random_dynamic_queue(size: int, min_val: int=0, max_val=100) -> DynamicQueue:
    """Generates a random dynamic queue of integers."""
    queue = DynamicQueue()
    for _ in range(size):
        queue.enqueue(random.randint(min_val, max_val))
    return queue

def random_deque(size: int, min_val: int=0, max_val=100) -> Deque:
    """Generates a random deque of integers."""
    deque = Deque(capacity=size)
    for _ in range(size):
        if random.choice([True, False]):
            deque.append_left(random.randint(min_val, max_val))
        else:
            deque.append_right(random.randint(min_val, max_val))
    return deque

def random_linked_list(size: int, min_val: int=0, max_val=100) -> LinkedList:
    """Generates a random linked list of integers."""
    linked_list = LinkedList()
    for _ in range(size):
        linked_list.append(random.randint(min_val, max_val))
    return linked_list

def random_doubly_linked_list(size: int, min_val: int=0, max_val=100) -> DoublyLinkedList:
    """Generates a random doubly linked list of integers."""
    doubly_linked_list = DoublyLinkedList()
    for _ in range(size):
        doubly_linked_list.append(random.randint(min_val, max_val))
    return doubly_linked_list

def random_binary_tree(n: int) -> 'Tree':
    """Generates a random binary tree.
    arguments:
    n -- number of nodes in the tree
    returns: 
    binary tree
    """
    tree = Tree()

    tree.root = random_binary_tree_node(n)

    return tree

def random_binary_tree_node(n: int) -> TreeNode:
    """Generates a random binary tree with exactly n nodes."""
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
    heap
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
    trie
    """
    from dsa.trie import Trie
    trie = Trie()
    for _ in range(n):
        word_length = random.randint(1, 10)
        word = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(word_length))
        trie.insert(word)
    return trie

def random_graph(n, density=0.1):
    pass
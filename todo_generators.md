class Stack:
    @classmethod
    def random(cls, size=10):
        return RandomGenerators.stack(size)


# random_generator.py
class RandomStructureGenerator:
    @staticmethod
    def random_list(size, min_val=0, max_val=100):
        return [random.randint(min_val, max_val) for _ in range(size)]

    @staticmethod
    def random_binary_tree(n):
        # generate tree nodes and link them up (for demo)
        ...

    @staticmethod
    def random_graph(n, density=0.2):
        ...
 
 class DSGenerator
    
    1. 
    Array
    DynamicArray
    
    2.
    Queue
    DynamicQueue
    Stack
    DynamicStack
    Deque
    
    3. HashTable??
    
    4.
    LinkedList
    DoublyLinkedList

    BinaryTree
    BinarySearchTree
    
    5.
    Heap
    Trie
    
    6.
    Graph (lots of variations)
    
    7.
    
    8.
    
    
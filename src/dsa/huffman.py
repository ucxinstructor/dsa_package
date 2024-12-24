""" Module to access functions for Huffman Compression. """
from dsa.tree import Tree, TreeNode
from dsa.heap import PriorityQueue

#import heapq

class Node:
    """ binary node implementation """
    def __init__(self, left, right, value=None):
        self.left = left
        self.right = right
        self.value = value
    
    def __lt__(self, other):
        return False
    
    def __repr__(self):
        if self.value is None:
            return "none"
        else:
            return self.value

def character_frequency(s: str) -> dict:
    """ 
    Takes a string a returns a dictionary of character frequencies.

    Args:
        s (str): The string to analyze.

    Returns:
        Dictionary containing character frequency.
    """
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d

def build_frequency_table(s: str) -> PriorityQueue:
    """ 
    Accepts a string to encode and returns a heap of the characters.

    Args:
        s (str): The string to encode.

    Returns:
        A priority queue of the characters based on frequencies.
    """
    frequency_dictionary = character_frequency(s)
    
    # add to priority queue
#    h = []
    pq = PriorityQueue()
#    for item in frequency_dictionary.items():
 #       pq.push(item[1], TreeNode(None, None, item[0]))
        #heapq.heappush(h, (item[1], Node(None, None, item[0])))

    for char, count in frequency_dictionary.items():
        pq.push(count, char) #item[1], TreeNode(None, None, item[0]))

    return pq

def build_huffman_tree(pq: PriorityQueue):
    """ 
    Accepts a heap and returns a Huffman Tree.

    Args:
        heap (list): A heap of characters based on frequencies. 

    Returns:
        A Huffman Tree.
    """
    while len(pq) > 1:
#    while len(heap) > 1:
#        n1 = heapq.heappop(heap)
 #       n2 = heapq.heappop(heap)
        n1 = pq.pop()
        n2 = pq.pop()
        print(n1)
        print(n2)
#        node = Node(n1[1], n2[1])
  #      heapq.heappush(heap, (n1[0] + n2[0], node))
 #       pq.push(n1[0] + n2[0], node)
#    return heap[0][1]
    return pq.pop()

def build_huffman_dictionary(node, bit_string: str=""):
    """
    Given a Huffman Node, build a Huffman Dictionary.

    Args:
        node (Node): The Huffman Node.
        bit_string (str): The bit string.

    Returns:
        A Huffman Dictionary.
    """
    d = {}
    if node.left is None and node.right is None:
        return {node.value: bit_string}

    d.update(build_huffman_dictionary(node.left, bit_string + '0'))
    d.update(build_huffman_dictionary(node.right, bit_string + '1'))

    return d

def huffman_encode(st: str, hd: dict):
    """
    Encode the string using the Huffman Dictionary.

    Args:
        st (str): The string to encode.
        hd (dict): The Huffman Dictionary.

    Returns:
        The encoded string.
    """
    s = ""
    for c in st:
        s += hd[c]
    return s

def huffman_decode(encoded_data, tree):
    """
    Decode the encoded data using the Huffman Tree.
    
    Args:
        encoded_data (str): The encoded data.
        tree (Node): The Huffman Tree.

    Returns:
        The decoded data.
    """

    root = tree
    s = ""
    for bit in encoded_data:
        if int(bit) == 0:
            tree = tree.left
        else:
            tree = tree.right

        if tree.left is None and tree.right is None: 
            s += tree.value
            tree = root
    return s

def bitstring_to_bytes(s: str):
    """
    Convert a bitstring to bytes.

    Args:
        s (str): The bitstring.

    Returns:
        Bitstring converted to bytes.
    """
    return bytes(int(s[i : i + 8], 2) for i in range(0, len(s), 8))

def bytes_to_bitstring(ba, bitlength=8):
    """
    Convert bytes to bitstring.

    Args:
        ba (bytes): The bytes to convert.
        bitlength (int): The bit length.
    
    Returns:
        The bytes converted to bitstring.
    """
    s = ""
    for b in ba[:-1]:
        byte = f"{b:08b}"
        s += byte
    
    byte = f"{ba[-1]:b}".zfill(bitlength) 
    s += byte

    return s



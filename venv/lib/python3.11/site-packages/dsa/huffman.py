""" Module to access functions for Huffman Compression. """
from dsa.tree import Tree, TreeNode
from dsa.heap import PriorityQueue

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
    
    pq = PriorityQueue()

    for char, count in frequency_dictionary.items():
        pq.push(count, TreeNode(char))#, None, None))

    return pq

def build_huffman_tree(pq: PriorityQueue) -> Tree:
    """ 
    Accepts a priority queue and returns a Huffman Tree.

    Args:
        pq (PriorityQueue): A PriorityQueue containing TreeNodes of characters based on frequencies. 

    Returns:
        A Huffman Tree.
    """
    while len(pq) > 1:
        priority1, node1 = pq.pop_pair()
        priority2, node2 = pq.pop_pair()
        node = TreeNode(node1.value + node2.value, node1, node2)
        pq.push(priority1 + priority2, node)

    return Tree(pq.pop())

def build_huffman_dictionary(node: TreeNode, bit_string: str="") -> dict:
    """
    Given a TreeNode, build a Huffman Dictionary.

    Args:
        node (TreeNode): The Huffman Node.
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

def huffman_encode(st: str, hd: dict) -> str:               
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

def huffman_decode(encoded_data: str, tree: Tree) -> str:
    """
    Decode the encoded data using the Huffman Tree.
    
    Args:
        encoded_data (str): The encoded data.
        tree (Tree): The Huffman Tree.

    Returns:
        The decoded data.
    """
    node = tree.root
    s = ""
    for bit in encoded_data:
        if int(bit) == 0:
            node = node.left
        else:
            node = node.right

        if node.left is None and node.right is None: 
            s += node.value
            node = tree.root
    return s

def bitstring_to_bytes(s: str) -> bytes:
    """
    Convert a bitstring to bytes.

    Args:
        s (str): The bitstring.

    Returns:
        Bitstring converted to bytes.
    """
    return bytes(int(s[i : i + 8], 2) for i in range(0, len(s), 8))

def bytes_to_bitstring(ba: bytes, bitlength: int=8) -> str:
    """
    Convert bytes to bitstring.

    Args:
        ba (bytes): The bytes to convert.
        bitlength (int): The bit length.
    
    Returns:
        The bytes converted to bitstring.
    """
    if not ba:
        return ""
    
    s = ""
    for b in ba[:-1]:
        byte = f"{b:08b}"
        s += byte
    
    byte = f"{ba[-1]:b}".zfill(bitlength) 
    s += byte

    return s

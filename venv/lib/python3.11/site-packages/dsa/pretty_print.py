""" Module to access functions for a clearer visual representation of certain data structures. """
import math

def heap_print(heap):
    """
    Print a heap from root to leaves.

    Args:
        heap: The heap object to print.
    """
    if not heap or heap.count() == 0:
        return

    _array_print(heap.count(), heap.enumerate())


def _array_print(node_count, enum_sequence):
    """
    Print a heap from root to leaves.

    Args:
        heap: The heap object to print.
    """
    height = math.floor(math.log2(node_count))
    level_str = ""
    current_level = 0
    value_width = 3
    max_width = 2 ** (height - 1) * value_width

    for index, node in enum_sequence:
        level = int(math.log2(index + 1))
        columns = 2 ** (level - 1)
        column_width = int(max_width / columns)
        if current_level != level:
            current_level = level
            print(level_str)
            level_str = ""
        level_str += f"{node:^{column_width}}"
    print(level_str)
    print()


def tree_to_array(node, index: int=0, tree_array=None):
    """
    (helper function) Create an array filled with index and value pairs from a node based tree.

    Args:
        node: The starting node.
        index (int): The starting index.
        tree_array: The destination array.

    Returns:
        Array filled with tree values.
    """
    if not tree_array:
        tree_array = []
    if node is None:
        return
    tree_array.append((index, node.value))
    tree_to_array(node.left, index * 2 + 1, tree_array)
    tree_to_array(node.right, index * 2 + 2, tree_array)
    
    return tree_array

def get_tree_height(node) -> int:
    """
    (helper function) Calculate the height of a tree.

    Args:
        node: The starting node.

    Returns:
        The height of a tree.
    """
    if node is None:
        return 0
    else:
        return max(get_tree_height(node.left) + 1, get_tree_height(node.right) + 1)

def fill_complete_tree(tree):
    """
    (helper function) Force a binary tree to be a complete tree by filling any empty nodes.

    Args:
        tree: The tree to fill.

    Returns:
        A new tree that is complete.
    """
    if tree is None:
        return None
    
    tree_array = tree_to_array(tree.root)
    if tree_array is None:
        return
    
    tree_height = get_tree_height(tree.root)

    # build empty complete tree
    array_size = (2 ** tree_height) - 1
    new_tree = [ "" ] * array_size

    # fill the complete tree array
    for index, value in tree_array:
        new_tree[index] = value
    return new_tree

def tree_print(tree):
    """
    Print a tree from root to leaves.

    Args:
        tree: The tree object to print.

    Notes:
        Reuses heap_print() by converting tree into a complete tree array.
    """
    complete_tree = fill_complete_tree(tree)
    if complete_tree:
        _array_print(len(complete_tree), enumerate(complete_tree))

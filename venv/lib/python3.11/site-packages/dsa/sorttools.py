""" Module to access functions for sort benchmarking. """
import random

def rand_int_array(n: int, maxnum: int) -> list:
    """ 
    Return an array of n integers of random numbers from 0 to maxnum.

    Args:
        n (int): The number of integers to generate.
        maxnum (int): The maximum number in a range (0-maxnum inclusive).
    Returns:
        Array of n integers of random numbers from 0 to maxnum.
    """
    array = [None] * n
    for i in range(n):
        array[i] = random.randint(0, maxnum)
    return array

def filled_array(n: int) -> list:
    """ 
    Return an array filled with integers from 0 to n-1.

    Args:
        n (int): the number of integers to generate.

    Returns:
        Array filled with integers from 0 to n-1.
    """
    array = [None] * n
    for i in range(n):
        array[i] = i
    return array    

def shuffle_array(n: int) -> list:
    """ 
    Return a shuffled array filled with integers from 0 to n-1.

    Args:
        n (int): The number of integers to generate.
    Returns:
        Array shuffled with integers from 0 to n-1.
    """
    array = filled_array(n)
    for i in range(n):
        r = random.randint(i, n-1)
        array[i], array[r] = array[r], array[i]
    return array

def is_sorted(array: list) -> bool:
    """ 
    Return a boolean on whether an array is sorted in ascending order or not.

    Args:
        array: the array to verify.
    Returns:
        True if the array is sorted, False otherwise.   
    """
    for i in range(len(array)-1):
        if array[i + 1] < array[i]:
            return False
    return True

def array_details(array: list) -> str:
    """
    Return a string with details about the array.
    Args:
        array: the array to analyze.
    Returns:
        A string with the count of elements, first 10 elements, and last 10 elements.
    """
    return f"Count: {len(array)} first 10: {array[:10]} last 10: {array[-10:]}"

def generate_almost_sorted_array(size: int, swaps: int) -> list:
    """
    Generate an almost sorted array of a given size with a specified number of swaps.   
    Args:
        size (int): The size of the array to generate.
        swaps (int): The number of adjacent elements to swap to create disorder.
    Returns:
        list: An array of integers that is mostly sorted with a few local swaps.
    """

    arr = list(range(size))
    for _ in range(swaps):
        i = random.randint(0, size - 2)
        arr[i], arr[i + 1] = arr[i + 1], arr[i]  # introduce a small local disorder
    return arr


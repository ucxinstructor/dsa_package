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

def is_sorted(array) -> bool:
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

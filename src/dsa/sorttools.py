""" Module to access functions for sort benchmarking. """
import random

def rand_int_array(n: int, maxnum: int) -> list:
    """ 
    return an array of n integers of random numbers from 0 to maxnum

    Args:
        n: the number of integers to generate
        maxnum: the maximum number in a range (0-maxnum inclusive)
    Returns:
    array of n integers of random numbers from 0 to maxnum
    """
    array = [None] * n
    for i in range(n):
        array[i] = random.randint(0, maxnum)
    return array

def filled_array(n):
    """ 
    return an array filled with integers from 0 to n-1

    Args:
        n: the number of integers to generate
    Returns:
    array filled with integers from 0 to n-1
    """
    array = [None] * n
    for i in range(n):
        array[i] = i
    return array    

def shuffle_array(n):
    """ 
    return a shuffled array filled with integers from 0 to n-1

    Args:
        n: the number of integers to generate
    Returns:
    array shuffled with integers from 0 to n-1
    """
    array = filled_array(n)
    for i in range(n):
        r = random.randint(i, n-1)
        array[i], array[r] = array[r], array[i]
    return array


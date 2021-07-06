"""
@Author: Ayur Ninawe
@Date: 2021-07-06 20:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-06 20:15:30
@Title : Write a Python program to get a list, sorted in increasing order by the last
element in each tuple from a given list of non-empty tuples.
"""

import loggerfile

def last(n): return n[-1]
"""
Description:
    Function to get last element of each tuple.
Return: last element of tuple 
"""
def sort_list_last(tuples):
    """
    Description:
        Function to get last element of each tuple.
    Parameter: 
        list of tuples
    Return: 
        sorted list of tuples
    """
    try:
        return sorted(tuples, key=last)
    except Exception :
        loggerfile.Logger("debug", "Invalid program")
    
if __name__ == '__main__': 
    print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
   
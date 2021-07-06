"""
@Author: Ayur Ninawe
@Date: 2021-07-06 20:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-06 20:15:30
@Title : Write a Python program to generate all permutations of a list in Python.
"""
import loggerfile
import itertools

def permute():
    
    """
    Description:
        Function to generate all permutations of a list in Python.
    Parameter:
        
    Return:
        
    """
    try:
        print(list(itertools.permutations([1,2,3])))
    except Exception :
        loggerfile.Logger("debug", "Invalid program")
    
permute()
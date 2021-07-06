"""
@Author: Ayur Ninawe
@Date: 2021-07-06 14:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-06 14:15:30
@Title : Write a Python program to reverse a string.
"""

import loggerfile

def reverse_string(str1):
    
    """
    Description:
        Function to reverse a string.
    Parameter:
        
    Return:
        
    """
    try:
        return ''.join(reversed(str1))
    except Exception :
        loggerfile.Logger("debug", "Invalid program")
print()
print(reverse_string("abcdef"))
print(reverse_string("Python Exercises."))
print()
    
    
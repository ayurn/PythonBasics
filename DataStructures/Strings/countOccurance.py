"""
@Author: Ayur Ninawe
@Date: 2021-07-06 14:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-06 14:15:30
@Title : Write a Python program to count occurrences of a substring in a string.
"""

import loggerfile

def occurrences():
    
    """
    Description:
        Function to count occurrences of a substring in a string.
  
    """
    try:

        str1 = 'The quick brown fox jumps over the lazy dog.'
        print()
        print(str1.count("fox"))
        print()
    except Exception :
        loggerfile.Logger("debug", "Invalid program")
        
occurrences()
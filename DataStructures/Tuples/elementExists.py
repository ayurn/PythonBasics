"""
@Author: Ayur Ninawe
@Date: 2021-07-05 21:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-05 21:15:30
@Title : Write a Python program to check whether an element exists within a tuple.
"""

import loggerfile

def exist():
    
    """
    Description:
        Function to check whether an element exists within a tuple.
    Parameter:
        
    Return:
        
    """
    try:
        tuplex = ("a", "y", "u", "r", 6, 2, 9, 9)
        print("r" in tuplex)
        print(5 in tuplex)
    except Exception :
        loggerfile.Logger("debug", "Invalid program")
        
if __name__ == '__main__':
    exist() 
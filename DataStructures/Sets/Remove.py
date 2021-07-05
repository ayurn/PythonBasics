"""
@Author: Ayur Ninawe
@Date: 2021-07-05 17:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-05 17:15:30
@Title : Write a Python program to remove item(s) from set
"""

import loggerfile

def remove():
    
    """
    Description:
        Function to remove first element of set
    Parameter:
        
    Return:
        
    """  
    try:
        num_set = set([0, 1, 3, 4, 5])
        print("Original set:")
        print(num_set)
        num_set.pop()
        print("\nAfter removing the first element from the said set:")
        print(num_set)
    except Exception :
        loggerfile.Logger("debug", "Invalid program")
        
if __name__ == '__main__':
    remove()
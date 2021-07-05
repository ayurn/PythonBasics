"""
@Author: Ayur Ninawe
@Date: 2021-07-05 20:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-05 20:15:30
@Title : Write a Python program to use of frozensets.
"""

import loggerfile

def frozenset():
    
    """
    Description:
        Function to use frozensets.
    Parameter:
        
    Return:   
    """
    try:        
        x = frozenset([1, 2, 3, 4, 5])
        y = frozenset([3, 4, 5, 6, 7])
        #use isdisjoint(). Return True if the set has no elements in common with other. 
        print(x.isdisjoint(y))
        #use difference(). Return a new set with elements in the set that are not in the others.
        print(x.difference(y))
        #new set with elements from both x and y
        print(x | y)
    except Exception :
       loggerfile.Logger("debug", "Invalid program")
       
if __name__ == '__main__':
    frozenset() 

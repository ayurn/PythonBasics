"""
@Author: Ayur Ninawe
@Date: 2021-07-05 17:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-05 17:15:30
@Title : Write a Python program to remove an item from a set if it is present in the set.
"""

import loggerfile

def removeItem():
    
    """
    Description:
        Function to remove element of set
    Parameter:
        
    Return:
        
    """  
    try:        
        
        #Create a new set
        num_set = set([0, 1, 2, 3, 4, 5])
        print("Original set elements:")
        print(num_set)
        print("\nRemove 0 from the said set:")
        num_set.discard(4)
        print(num_set)
        print("\nRemove 5 from the said set:")
        num_set.discard(5)
        print(num_set)
        print("\nRemove 2 from the said set:")
        num_set.discard(5)
        print(num_set)
        print("\nRemove 7 from the said set:")
        num_set.discard(15)
        print(num_set)
    except Exception :
        loggerfile.Logger("debug", "Invalid program")
        
if __name__ == '__main__':
    removeItem()
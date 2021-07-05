"""
@Author: Ayur Ninawe
@Date: 2021-07-05 21:30:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-05 21:30:30
@Title : Write a Python program to reverse a tuple.
"""

import loggerfile

def reverse():
    
    """
    Description:
        Function to reverse a tuple.
    Parameter:
        
    Return:
        
    """
    try:
        #create a tuple
        strtuple = ("ayur")
        # Reversed the tuple
        strtuples = reversed(strtuple)
        print(tuple(strtuples))
        #create another tuple
        stringnum = (5, 10, 15, 20)
        # Reversed the tuple
        numstring = reversed(stringnum)
        print(tuple(numstring))
    except Exception :
        loggerfile.Logger("debug", "Invalid program")
        
if __name__ == '__main__':
    reverse() 

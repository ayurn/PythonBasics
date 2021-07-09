"""
@Author: Ayur Ninawe
@Date: 2021-07-05 21:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-05 21:15:30
@Title : Write a Python program to find the repeated items of a tuple.
"""

import loggerfile

def repeatedItem():
    
    """
    Description:
        Function to find the repeated items of a tuple.

    """
    try:
        #create a tuple
        tuplex = 2, 4, 5, 6, 2, 3, 4, 4, 7 
        print(tuplex)
        #return the number of times it appears in the tuple.
        count = tuplex.count(4)
        print(count)
    except Exception :
        loggerfile.Logger("debug", "Invalid program")
        
if __name__ == '__main__':
    repeatedItem() 
"""
@Author: Ayur Ninawe
@Date: 2021-07-05 21:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-05 21:15:30
@Title : Write a Python program to unpack a tuple in several variables.
"""

import loggerfile

def unpackTuple():
    
    """
    Description:
        Function to unpack a tuple in several variables.
    Parameter:
        
    Return:
        
    """
    try:
        #create a tuple
        tuplex = 4, 8, 3 
        print(tuplex)
        n1, n2, n3 = tuplex
        #unpack a tuple in variables
        print(n1 + n2 + n3) 
        #the number of variables must be equal to the number of items of the tuple
        n1, n2, n3, n4= tuplex
    except Exception :
        loggerfile.Logger("debug", "Invalid program")
        
if __name__ == '__main__':
    unpackTuple() 
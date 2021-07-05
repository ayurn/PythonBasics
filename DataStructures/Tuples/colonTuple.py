"""
@Author: Ayur Ninawe
@Date: 2021-07-05 21:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-05 21:15:30
@Title : Write a Python program to create the colon of a tuple.
"""

import loggerfile

def colonTuple():
    
    """
    Description:
        Function to create the colon of a tuple.
    Parameter:
        
    Return:
        
    """
    try:
        from copy import deepcopy
        #create a tuple
        tuplex = ("HELLO", 5, [], True) 
        print(tuplex)
        #make a copy of a tuple using deepcopy() function
        tuplex_colon = deepcopy(tuplex)
        tuplex_colon[2].append(50)
        print(tuplex_colon)
        print(tuplex)
    except Exception :
        loggerfile.Logger("debug", "Invalid program")
        
if __name__ == '__main__':
    colonTuple() 
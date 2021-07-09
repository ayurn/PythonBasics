"""
@Author: Ayur Ninawe
@Date: 2021-07-05 21:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-05 21:15:30
@Title : Write a Python program to create a tuple.
"""

import loggerfile

def createTuple():
    
    """
    Description:
        Function to create create a tuple.
 
    """
    try:
        #Create a tuple with different data types
        tuplex = ("tuple", False, 3.2, 1)
        print(tuplex)
    except Exception :
       loggerfile.Logger("debug", "Invalid program")
       
if __name__ == '__main__':
    createTuple() 
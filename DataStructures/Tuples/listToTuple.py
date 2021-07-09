"""
@Author: Ayur Ninawe
@Date: 2021-07-05 21:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-05 21:15:30
@Title : Write a Python program to convert a list to a tuple.
"""

import loggerfile

def listToTuple():
    
    """
    Description:
        Function to convert a list to a tuple.
 
    """
    try:
        #Convert list to tuple
        listx = [5, 10, 7, 4, 15, 3]
        print(listx)
        #use the tuple() function built-in Python, passing as parameter the list
        tuplex = tuple(listx)
        print(tuplex)
    except Exception :
        loggerfile.Logger("debug", "Invalid program")
        
if __name__ == '__main__':
    listToTuple() 
"""
@Author: Ayur Ninawe
@Date: 2021-07-05 21:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-05 21:15:30
@Title : Write a Python program to remove an item from a tuple.
"""

import loggerfile

def removeItem():
    
    """
    Description:
        Function to remove an item from a tuple.
    Parameter:
        
    Return:
        
    """
    try:
        #create a tuple
        tuplex = ("a", "y", "u", "r", "n", "i", "n", "a", "w", "e")
        print(tuplex)
        #tuples are immutable, so we can not remove elements
        #using merge of tuples with the + operator you can remove an item and it will create a new tuple
        tuplex = tuplex[:2] + tuplex[3:]
        print(tuplex)
        #converting the tuple to list
        listx = list(tuplex) 
        #use different ways to remove an item of the list
        listx.remove("e") 
        #converting the tuple to list
        tuplex = tuple(listx)
        print(tuplex)
    except Exception :
        loggerfile.Logger("debug", "Invalid program")
        
if __name__ == '__main__':
    removeItem() 
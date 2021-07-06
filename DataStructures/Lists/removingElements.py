"""
@Author: Ayur Ninawe
@Date: 2021-07-06 20:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-06 20:15:30
@Title : Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
"""

import loggerfile

def removeItem():
    
    """
    Description:
        Function to print a specified list after removing the 0th, 4th and 5th elements.
    Parameter:
        
    Return:
        
    """
    try:
        color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
        color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
        print(color)
    except Exception :
        loggerfile.Logger("debug", "Invalid program")
    
if __name__ == '__main__':    
    removeItem()
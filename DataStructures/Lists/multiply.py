"""
@Author: Ayur Ninawe
@Date: 2021-07-06 20:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-06 20:15:30
@Title : Write a Python program to multipy all the items in a list.
"""

import loggerfile

def multiply_list(items):
    
    """
    Description:
        Function to multipy all the items in a list.

    """
    try:
        tot = 1
        for x in items:
            tot *= x
        return tot
    except Exception :
        loggerfile.Logger("debug", "Invalid program")
    
if __name__ == '__main__':    
    print(multiply_list([1,2,-8]))
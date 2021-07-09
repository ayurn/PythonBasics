"""
@Author: Ayur Ninawe
@Date: 2021-07-06 20:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-06 20:15:30
@Title : Write a Python program to sum all the items in a list.
"""

import loggerfile

def sum_list(items):
    
    """
    Description:
        Function to sum all the items in a list.
 
    """
    try:
        sum_numbers = 0
        for x in items:
            sum_numbers += x
        return sum_numbers
    except Exception :
        loggerfile.Logger("debug", "Invalid program")
    
if __name__ == '__main__':    
    print(sum_list([1,2,-8]))
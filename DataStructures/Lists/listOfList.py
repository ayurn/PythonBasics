"""
@Author: Ayur Ninawe
@Date: 2021-07-06 20:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-06 20:15:30
@Title : Write a Python program to remove duplicates from a list of lists.
"""

import loggerfile

def duplicateList():
    
    """
    Description:
        Function to remove duplicates from a list of lists.

    """
    try:
        import itertools
        num = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
        print("Original List", num)
        num.sort()
        new_num = list(num for num,_ in itertools.groupby(num))
        print("New List", new_num)
    except Exception :
        loggerfile.Logger("debug", "Invalid program")
        
duplicateList()
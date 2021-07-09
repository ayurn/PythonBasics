"""
@Author: Ayur Ninawe
@Date: 2021-07-06 20:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-06 20:15:30
@Title : Write a Python program to append a list to the second list.
"""

import loggerfile

def append():
    
    """
    Description:
        Function to append a list to the second list.
       
    """
    try:
        list1 = [1, 2, 3, 0]
        list2 = ['Red', 'Green', 'Black']
        final_list = list1 + list2
        print(final_list)
    except Exception :
        loggerfile.Logger("debug", "Invalid program")
        
append()
"""
@Author: Ayur Ninawe
@Date: 2021-07-06 20:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-06 20:15:30
@Title : Write a Python program to get the difference between the two lists.
"""

import loggerfile

def difference(): 
    """
    Description:
        Function to get the difference between the two lists.

    """
    try:
        list1 = [1, 3, 5, 7, 9]
        list2=[1, 2, 4, 6, 7, 8]
        diff_list1_list2 = list(set(list1) - set(list2))
        diff_list2_list1 = list(set(list2) - set(list1))
        total_diff = diff_list1_list2 + diff_list2_list1
        print(total_diff)
    except Exception :
        loggerfile.Logger("debug", "Invalid program")
        
difference()
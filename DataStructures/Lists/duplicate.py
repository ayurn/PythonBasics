"""
@Author: Ayur Ninawe
@Date: 2021-07-06 20:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-06 20:15:30
@Title : Write a Python program to remove duplicates from a list.
"""

import loggerfile

def Duplicate():
    
    """
    Description:
        Function to remove duplicates from a list.

    """
    try:
        a = [10,20,30,20,10,50,60,40,80,50,40]

        dup_items = set()
        uniq_items = []
        for x in a:
            if x not in dup_items:
                uniq_items.append(x)
                dup_items.add(x)

        print(dup_items)
    except Exception :
        loggerfile.Logger("debug", "Invalid program")
 
Duplicate()
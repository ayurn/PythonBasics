"""
@Author: Ayur Ninawe
@Date: 2021-07-06 20:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-06 20:15:30
@Title : Write a Python function that takes two lists and returns True if they have at
least one common member.
"""

import loggerfile

def common_data(list1, list2):
    
    """
    Description:
        function that takes two lists and returns True if they have at
        least one common member.
    Parameter:
        accept two lists.        
    Return:
        result of function.
        
    """
    try:
        result = False
        for x in list1:
            for y in list2:
                if x == y:
                    result = True
                    return result
    except Exception :
        loggerfile.Logger("debug", "Invalid program")
             
             
print(common_data([1,2,3,4,5], [5,6,7,8,9]))
print(common_data([1,2,3,4,5], [6,7,8,9]))
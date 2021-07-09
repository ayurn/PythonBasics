"""
@Author: Ayur Ninawe
@Date: 2021-07-06 20:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-06 20:15:30
@Title : Write a Python program to get the smallest number from a list.
"""

import loggerfile

def smallest_num_in_list( list ):
    
    """
    Description:
        Function to get the smallest number from a list.

    """
    try:
        min = list[ 0 ]
        for a in list:
            if a < min:
                min = a
        return min
    except Exception :
        loggerfile.Logger("debug", "Invalid program")
    
if __name__ == '__main__':    
    print(smallest_num_in_list([1, 2, -8, 0]))
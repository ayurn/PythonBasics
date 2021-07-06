"""
@Author: Ayur Ninawe
@Date: 2021-07-06 20:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-06 20:15:30
@Title : Write a Python program to clone or copy a list.
"""

import loggerfile

def clone():
    
    """
    Description:
        Function to clone or copy a list.
    Parameter:
        
    Return:
        
    """
    try:
        original_list = [10, 22, 44, 23, 4]
        new_list = list(original_list)
        print(original_list)
        print(new_list)
    except Exception :
        loggerfile.Logger("debug", "Invalid program")
    
if __name__ == '__main__':    
    clone()
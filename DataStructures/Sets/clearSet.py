"""
@Author: Ayur Ninawe
@Date: 2021-07-05 20:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-05 20:15:30
@Title : Write a Python program to clear a set.
"""

import loggerfile

def clear():
    """
    Description:
        Function to clear a set.
    Parameter:
        
    Return:
        
    """
    try:
        # set of letters
        charset = {'a', 'y', 'u', 'r', 'n'}
        print('set before clear:', charset)
        
        # clearing set
        charset.clear()
        print('set after clear:', charset)
    except Exception :
       loggerfile.Logger("debug", "Invalid program")
       
if __name__ == '__main__':
    clear() 
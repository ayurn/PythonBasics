"""
@Author: Ayur Ninawe
@Date: 2021-07-06 14:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-06 14:15:30
@Title : Write a Python program to get the last part of a string before a specified character.
"""

import loggerfile

def get_last_part():
    
    """
    Description:
        Function to get the last part of a string before a specified character.
    Parameter:
        
    Return:
        
    """
    try:
        str1 = 'https://www.ayurn.com/python-exercises/string'
        print(str1.rsplit('/', 1)[0])
        print(str1.rsplit('-', 1)[0])
    except Exception :
        loggerfile.Logger("debug", "Invalid program")
        
get_last_part()        

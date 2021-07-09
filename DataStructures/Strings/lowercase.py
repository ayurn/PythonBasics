"""
@Author: Ayur Ninawe
@Date: 2021-07-06 14:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-06 14:15:30
@Title : Write a Python program to lowercase first n characters in a string.
"""

import loggerfile

def lowercase():
    
    """
    Description:
        Function to lowercase first n characters in a string.

    """
    try:

        str1 = 'HAPPIESTMINDS.COM'
        print(str1[:4].lower() + str1[4:])
    except Exception :
        loggerfile.Logger("debug", "Invalid program")

lowercase()
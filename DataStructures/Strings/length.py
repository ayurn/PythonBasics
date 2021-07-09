"""
@Author: Ayur Ninawe
@Date: 2021-07-06 14:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-06 14:15:30
@Title : Write a Python program to calculate the length of a string.
"""

import loggerfile

def string_length(str1):
    
    """
    Description:
        Function to calculate the length of a string.

    """
    try:
        count = 0
        for char in str1:
            count += 1
        return count
    except Exception :
        loggerfile.Logger("debug", "Invalid program")
    
if __name__ == '__main__':    
    print(string_length('Ayurninawe'))
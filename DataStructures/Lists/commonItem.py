"""
@Author: Ayur Ninawe
@Date: 2021-07-06 20:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-06 20:15:30
@Title : Write a Python program to find common items from two lists.
"""

import loggerfile

def common():
    
    """
    Description:
        Function to find common items from two lists.
    Parameter:
        
    Return:
        
    """
    try:
        color1 = "Red", "Green", "Orange", "White"
        color2 = "Black", "Green", "White", "Pink"
        print(set(color1) & set(color2))
    except Exception :
        loggerfile.Logger("debug", "Invalid program")
        
common()
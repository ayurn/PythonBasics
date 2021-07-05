"""
@Author: Ayur Ninawe
@Date: 2021-07-05 17:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-05 17:15:30
@Title : Write a Python program to create an intersection of sets.
"""

import loggerfile

def intersection():
    
    """
    Description:
        Function to create different types of set
    Parameter:
        
    Return:
        
    """   
    try:
        setx = set(["green", "blue"])
        sety = set(["blue", "red"])
        print("Original set elements:")
        print(setx)
        print(sety)
        print("\nIntersection of two said sets:")
        setz = setx & sety
        print(setz)
    except Exception :
        loggerfile.Logger("debug", "Invalid program")
if __name__ == '__main__':
    intersection()
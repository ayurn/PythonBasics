"""
@Author: Ayur Ninawe
@Date: 2021-07-05 17:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-05 17:15:30
@Title : Write a Python program to create a union of sets.
"""

import loggerfile

def union():
    
    """
    Description:
        Function to create a union of sets.
    Parameter:
        
    Return:
        
    """
    
    try:        
        setc1 = set(["green", "blue"])
        setc2 = set(["blue", "red"])
        print("Original sets:")
        print(setc1)
        print(setc2)
        setc = setc1.union(setc2)
        print("\nUnion of above sets:")
        print(setc)
        setn1 = set([1, 1, 2, 3, 4, 5])
        setn2 = set([1, 5, 6, 7, 8, 9])
        print("\nOriginal sets:")
        print(setn1)
        print(setn2)
        print("\nUnion of above sets:")
        setn = setn1.union(setn2)
        print(setn)
    except Exception :
       loggerfile.Logger("debug", "Invalid program")
       
if __name__ == '__main__':
    union() 
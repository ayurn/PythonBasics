"""
@Author: Ayur Ninawe
@Date: 2021-07-05 17:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-05 17:15:30
@Title : Write a Python program to create set difference.
"""

import loggerfile

def difference():
    
    """
    Description:
        Function to create set difference.
    Parameter:
        
    Return:
        
    """   
    try:      
        setc1 = set(["green", "blue"])
        setc2 = set(["blue", "red"])
        print("Original sets:")
        print(setc1)
        print(setc2)
        r1 = setc1.difference(setc2)
        print("\nDifference of setc1 - setc2:")
        print(r1)
        r2 = setc2.difference(setc1)
        print("\nDifference of setc2 - setc1:")
        print(r2)
        setn1 = set([1, 1, 2, 3, 4, 5])
        setn2 = set([1, 5, 6, 7, 8, 9])
        print("\nOriginal sets:")
        print(setn1)
        print(setn2)
        r1 = setn1.difference(setn2)
        print("\nDifference of setn1 - setn2:")
        print(r1)
        r2 = setn2.difference(setn1)
        print("\nDifference of setn2 - setn1:")
        print(r2)
    except Exception :
       loggerfile.Logger("debug", "Invalid program")
       
if __name__ == '__main__':
    difference() 

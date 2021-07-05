"""
@Author: Ayur Ninawe
@Date: 2021-07-05 17:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-05 17:15:30
@Title : Write a Python program to create a set.
"""

import loggerfile

def createSet():
    
    """
    Description:
        Function to create different types of set
    Parameter:
        
    Return:
        
    """
    
    try:
        print("Create a new set:")
        x = set()
        print(x)
        print(type(x))
        print("\nCreate a non empty set:")
        n = set([0, 1, 2, 3, 4])
        print(n)
        print(type(n))
        print("\nUsing a literal:")
        a = {1,2,3,'food','bar'}
        print(type(a))
        print(a)
    except Exception as e:
        loggerfile.Logger("debug", "Invalid program")
        
if __name__ == '__main__':
    createSet()
"""
@Author: Ayur Ninawe
@Date: 2021-07-05 17:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-05 17:15:30
@Title : Write a Python program to create a set.
"""

import loggerfile

def iterate():
    
    """
    Description:
        Function to iterate through of set
    Parameter:
        
    Return:
        
    """
    
    try:
        #Create a set 
        num_set = set([0, 1, 2, 3, 4, 5])
        for n in num_set:
            print(n, end=' ')
        print("\n\nCreating a set using string:")
        char_set = set("AyurNinawe")  
        # Iterating using for loop
        for val in char_set:
            print(val, end=' ')
    except Exception :
        loggerfile.Logger("debug", "Invalid program")
        
if __name__ == '__main__':
    iterate()
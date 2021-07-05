"""
@Author: Ayur Ninawe
@Date: 2021-07-05 20:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-05 20:15:30
@Title : Write a Python program to find maximum and the minimum value in a set.
"""
import loggerfile

def minmax():
    
    """
    Description:
        Function to find maximum and the minimum value in a set.
    Parameter:
        
    Return: 
    """
    try:        
        #Create a set
        setn = {5, 10, 3, 15, 2, 20}
        print("Original set elements:")
        print(setn)
        print(type(setn))
        print("\nMaximum value of the said set:")
        print(max(setn))
        print("\nMinimum value of the said set:")
        print(min(setn))
    except Exception :
       loggerfile.Logger("debug", "Invalid program")
       
if __name__ == '__main__':
    minmax()
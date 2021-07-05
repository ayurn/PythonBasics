
"""
@Author: Ayur Ninawe
@Date: 2021-07-05 17:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-05 17:15:30
@Title : Write a Python program to add member(s) in a set.
"""

import loggerfile

def add():
    
    """
    Description:
        Function to add member in set.
    Parameter:
        
    Return:
        
    """
    try:
        #A new empty set
        name_set = set()
        print(name_set)
        print("\nAdd single element:")
        name_set.add("Ayur")
        print(name_set)
        print("\nAdd multiple items:")
        name_set.update(["Anuj", "Tanmay"])
        print(name_set)
    except Exception :
       loggerfile.Logger("debug", "Invalid program")
       
if __name__ == '__main__':
    add() 
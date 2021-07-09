"""
@Author: Ayur Ninawe
@Date: 2021-07-04 20:30:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-04 20:30:30
@Title : Write a Python program to count number of items in a dictionary value that is a list.

"""

import loggerfile

def main():
    """
        Description:
            Function to count number of items in a dictionary value that is a list.
        array.
        """
    try:
        # defining the dictionary
        d = {'A' : [1, 2, 3, 4, 5, 6, 7, 8, 9],
            'B' : 34,
            'C' : 12,
            'D' : [7, 8, 9, 6, 4] }
    
        # using the in operator
        count = 0
        for x in d:
            if isinstance(d[x], list):
                count += len(d[x])
        print(count)
    except Exception :
        loggerfile.Logger("debug", "Invalid")
  
# Calling Main    
if __name__ == '__main__':
    main()
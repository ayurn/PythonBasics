"""
@Author: Ayur Ninawe
@Date: 2021-07-04 18:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-04 18:15:30
@Title : Write a Python program to print a dictionary in table format.
"""

import loggerfile

def table():
    """
        Description:
            Function to print a dictionary in table format.
        """
    try:
        my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
        for row in zip(*([key] + (value) for key, value in sorted(my_dict.items()))):
            print(*row)
    except Exception :
        loggerfile.Logger("debug", "Invalid")
        
if __name__ == '__main__':
    table()                    
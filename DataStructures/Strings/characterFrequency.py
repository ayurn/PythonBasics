"""
@Author: Ayur Ninawe
@Date: 2021-07-06 14:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-06 14:15:30
@Title : Write a Python program to count the number of characters (character frequency) in a
string.
"""

import loggerfile

def char_frequency(str1):
    
    """
    Description:
        Function to count the number of characters (character frequency) in a
        string.
    Parameter:
        str1 : string as input.
    Return:
       dict : dictionary with character count 
    """
    try: 
        dict = {}
        for n in str1:
            keys = dict.keys()
            if n in keys:
                dict[n] += 1
            else:
                dict[n] = 1
        return dict
    except Exception :
        loggerfile.Logger("debug", "Invalid program")
        
if __name__ == '__main__':
    print(char_frequency('google.com'))
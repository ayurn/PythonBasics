"""
@Author: Ayur Ninawe
@Date: 2021-07-06 14:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-06 14:15:30
@Title : Write a Python program to add 'ing' at the end of a given string (length should be at
least 3). If the given string already ends with 'ing' then add 'ly' instead. 
If the string length of thegiven string is less than 3, leave it unchanged.
"""

import loggerfile

def add_string(str1):
    """
    Description:
        Function to add string at end.
    """
    try:
        length = len(str1)

        if length > 2:
            if str1[-3:] == 'ing':
                str1 += 'ly'
            else:
                str1 += 'ing'

        return str1
    except Exception :
        loggerfile.Logger("debug", "Invalid program")

if __name__ == '__main__':
    print(add_string('ab'))
    print(add_string('abc'))
    print(add_string('string'))
"""
@Author: Ayur Ninawe
@Date: 2021-07-06 14:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-06 14:15:30
@Title : Write a Python program to get a string from a given string where all occurrences of its
first char have been changed to '$', except the first char itself.
"""
import loggerfile

def change_char(str1):
    """
    Description:
        Function to change all occurrences of its first char have been changed to '$', 
        except the first char itself.
    Parameter:
        str1 : string input
    Return:
        str1 : string output
    """
    
    try:
        char = str1[0]
        str1 = str1.replace(char, '$')
        str1 = char + str1[1:]

        return str1
    except Exception :
        loggerfile.Logger("debug", "Invalid program")

if __name__ == '__main__':
    print(change_char('restart'))
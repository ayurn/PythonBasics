"""
@Author: Ayur Ninawe
@Date: 2021-07-06 14:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-06 14:15:30
@Title : Write a Python script that takes input from the user and displays that input back in upper and lower cases.
"""

import loggerfile

def uppperLower() :
    """
    Description:
        Function to take input from the user and displays that input back in upper and lower cases.

    """
    try:
        user_input = input("What's your favourite language? ")
        print("My favourite language is ", user_input.upper())
        print("My favourite language is ", user_input.lower())
    except Exception :
        loggerfile.Logger("debug", "Invalid program")

if __name__ == '__main__':
    uppperLower()
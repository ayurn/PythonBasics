"""
@Author: Ayur Ninawe
@Date: 2021-07-06 14:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-06 14:15:30
@Title : Write a Python program that accepts a comma separated sequence of words as input
and prints the unique words in sorted form (alphanumerically).
"""

import loggerfile

def commaSeparated():
    """
    Description:
        Function that accepts a comma separated sequence of words as input
        and prints the unique words in sorted form.

    """
    try:
        items = input("Input comma separated sequence of words")
        words = [word for word in items.split(",")]
        print(",".join(sorted(list(set(words)))))
    except Exception :
        loggerfile.Logger("debug", "Invalid program")
        
commaSeparated()
        
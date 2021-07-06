"""
@Author: Ayur Ninawe
@Date: 2021-07-06 14:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-06 14:15:30
@Title : Write a Python program to display formatted text (width=50) as output.
"""

import loggerfile

def format_text(str1):
    
    """
    Description:
        Function to display formatted text (width=50) as output.
    Parameter:
        
    Return:
        
    """
    try:
        import textwrap
        sample_text = '''
        Python is a widely used high-level, general-purpose, interpreted,
        dynamic programming language. Its design philosophy emphasizes
        code readability, and its syntax allows programmers to express
        concepts in fewer lines of code than possible in languages such
        as C++ or Java.
        '''
        print()
        print(textwrap.fill(sample_text, width=50))
        print()
    except Exception :
        loggerfile.Logger("debug", "Invalid program")

format_text()
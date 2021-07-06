"""
@Author: Ayur Ninawe
@Date: 2021-07-03 18:25:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-03 18:25:30
@Title : Write a Python program to remove the first occurrence of a specified element from an
        array.
"""

import array as arr 
import loggerfile

class Arrayelement():
    def display(self):
        try:
            ar = arr.array('i', [1, 3, 5, 3, 7, 1, 9, 3])
            ar.remove(3)
            print(ar)
        except Exception :
            loggerfile.Logger("debug", "Invalid")
        
if __name__ == '__main__':
    Arrayelement.display(0)
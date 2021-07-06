"""
@Author: Ayur Ninawe
@Date: 2021-07-03 18:20:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-03 18:20:30
@Title : Write a Python program to get the number of occurrences of a specified element in an
         array.
"""

import array as arr 
import loggerfile

class Arrayelement():
    def display(self):
        try:
            ar = arr. array('i', [1, 3, 5, 3, 7, 9, 3])
            print(ar.count(3))
        except Exception :
            loggerfile.Logger("debug", "Invalid")
        
if __name__ == '__main__':
    Arrayelement.display(0)
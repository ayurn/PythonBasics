"""
@Author: Ayur Ninawe
@Date: 2021-07-03 18:20:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-03 18:20:30
@Title : Write a Python program to reverse the order of the items in the array.
"""

import array as arr 
import loggerfile

class Arrayelement():
    def display(self):
        try:
            ar = arr.array('i', [1, 3, 5, 9, 7])
            ar.reverse()
            print(ar)  
        except Exception as e:
            loggerfile.Logger("debug", print(e))     
        
if __name__ == '__main__':
    Arrayelement.display(0)
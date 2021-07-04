"""
@Author: Ayur Ninawe
@Date: 2021-07-03 18:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-03 18:15:30
@Title : appending element at end.
"""

import array as arr
import loggerfile

class Arrayelement():
    try:
        def display(self):
            ar = arr.array('i', [1, 3, 5, 9, 7])
            ar.append(69)
            print(ar)
    except Exception as e:
        loggerfile.Logger("debug", print(e))

        
if __name__ == '__main__':
    Arrayelement.display(0)
"""
@Author: Ayur Ninawe
@Date: 2021-07-03 18:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-03 18:15:30
@Title : Write a Python script to add a key to a dictionary.
"""
import loggerfile

def addKey():
    try:
        d = {0:10, 1:20}
        print(d)
        d.update({2:30})
        print(d)
    except Exception :
        loggerfile.Logger("debug", "Invalid")
    
if __name__ == '__main__':
    addKey()
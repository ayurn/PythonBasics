"""
@Author: Ayur Ninawe
@Date: 2021-07-04 20:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-04 20:15:30
@Title :Write a Python program to check multiple keys exists in a dictionary.
"""

import loggerfile

def keys():
    try:
        student = {
        'name': 'Alex',
        'class': 'V',
        'roll_id': '2'
        }
        print(student.keys() >= {'class', 'name'})
        print(student.keys() >= {'name', 'Alex'})
        print(student.keys() >= {'roll_id', 'name'})
    except Exception :
        loggerfile.Logger("debug", "Invalid")
        
if __name__ == '__main__':
    keys()
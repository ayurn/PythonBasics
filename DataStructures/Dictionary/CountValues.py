 
"""
@Author: Ayur Ninawe
@Date: 2021-07-04 20:30:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-04 20:30:30
@Title : Write a Python program to count the values associated with key in a dictionary.

"""        
import loggerfile
        
def countValue():
    try:        
        student = [{'id': 1, 'success': True, 'name': 'Lary'},
        {'id': 2, 'success': False, 'name': 'Rabi'},
        {'id': 3, 'success': True, 'name': 'Alex'}]
        print(sum(d['id'] for d in student))
        print(sum(d['success'] for d in student))
    except Exception :
        loggerfile.Logger("debug", "Invalid")
        
if __name__ == '__main__':
    countValue()
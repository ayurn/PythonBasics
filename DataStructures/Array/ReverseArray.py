import array as arr 

class Arrayelement():
    def display(self):
        ar = arr.array('i', [1, 3, 5, 9, 7])
        ar.reverse()
        print(ar)       
        
if __name__ == '__main__':
    Arrayelement.display(0)
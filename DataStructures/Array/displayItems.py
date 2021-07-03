import array as arr

class Arrayelement():
    def display(self):
        ar = arr.array('i', [1, 3, 5, 9, 7])
        print(ar)
        print(ar[0])
        print(ar[3])
        
if __name__ == '__main__':
    Arrayelement.display(0)
from multiprocessing import Pipe


"""Dealing with blocking of program due to recv()"""


def main():
    f, e = Pipe()
    
    e.send('item-1')
    e.send('item-2')
    
    for i in range(5):
        
        if f.poll():
            obj = f.recv()
            print(obj, 'has received.')
        else:
            print('Nothing is received.')    
        
        
        
if __name__ == '__main__':
    main()
    
    

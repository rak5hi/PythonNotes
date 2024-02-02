from typing import Protocol

class Printable(Protocol):
    pages: int
    
    def print(self):
        pass
   
    def recycle(self):
        pass
    
class Book:
    pages: int
    
    def __init__(self, title: str):
        self.title = title
        
    def print(self):
        print("printing book", self.title)
   
    def recycle(self):
        print("recycling book", self.title)
        
class Magazine:
    pages: int
    
    def __init__(self, title: str):
        self.title = title
        
    def print(self):
        print("printing magazine", self.title)
   
    def recycle(self):
        print("recycling magazine", self.title)

def print_object(obj: Printable):
    obj.print()   
         
book: Printable = Book("Python")
magazine: Printable = Magazine("Mag....")

#instead of:
#book.print()
#maganize.print()

print_object(book)
print_object(magazine)


#class Book and Magazine must contain same/all
# methods as in prototype-class Printable, but
#class Book,Magazine.. may contain extra methods
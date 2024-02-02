class Parent:
    def __init__(self, name: str):
        self.name = name
        
    def class_print(self):
        print("This is Prent class..\n")
        
        
class Child(Parent):
    def __init__(self, name: str, parent_name: str):
        super().__init__(name)
        self.parent_name = parent_name
        
    def class_print(self):
        super().class_print()
        print("This is Child class..\n")
        
#creating ba instance
c1: Child = Child("child1", "parent1")
c1.class_print()
print(c1.name)


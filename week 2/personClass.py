class Person:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return self.name
    
        
p1=Person("ado")
print(p1)

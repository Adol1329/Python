class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender=gender
        self.age=age
        
        
    def __str__(self):
        return self.name
        return self.gender
        return self.age
    
        
p1=Person("ado","male","10")
print(p1.name)
print(p1.gender)
print(p1.age)
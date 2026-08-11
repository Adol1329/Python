class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender=gender
        self.age=age    

    def set_name(self, name):
        self.name=name
    def get_name(self):
        return self.name
        
p1 = Person("Adol", "Male", 20)
p1.set_name("Dan")
print(p1.get_name())
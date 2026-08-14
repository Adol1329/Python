"""
Create a class Person with:
● name
● age
● introduce() → displays the person's name and age.
Then create a class Student that inherits from Person.
Add:
● student_id
● study() → displays "I am studying Python".
Example usage:
student = Student("John", 21, "ST001")
student.introduce()
student.study()
"""


class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        
    def introduce(self):   
        return f"My name is {self.name}. \n I am {self.age} years old"

class Student(Person):
    def __init__(self,name,age, student_id):
        super().__init__(name)
          
        
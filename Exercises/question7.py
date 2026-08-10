"""
Exercise 7: Logical Operators
Given:
age = 22
has_id = True
Check whether the person is allowed to enter using:
● and
● or
● not
"""
age = 22
has_id = True
if age >= 18 and has_id:
    print("Allowed to enter")
else:
    print("Not allowed to enter")
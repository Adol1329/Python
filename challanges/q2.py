"""
Question 2: Username Generator (String)

Ask the user to enter:

* First name
* Last name

Generate a username by combining the first name and last name in lowercase.

Example:

Input:
First Name: John
Last Name: Doe
Output:
Username: johndoe

⸻
"""

firstName= input("Enter first name: \n")
lastName= input("enter last name: \n")
username= f"{firstName.lower()} {lastName.lower()}"
print(username)

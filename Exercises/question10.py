# Exercise 10: Student Result

math = float(input("Enter Math: "))
english = float(input("Enter English: "))
science = float(input("Enter Science: "))

total = math + english + science
average = total / 3
passed = average >= 20

print("Total:", total)
print("Average:", average)
print("Passed:", passed)
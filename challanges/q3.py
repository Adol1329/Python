"""
Question 3: Shopping List (List)

Create a shopping list containing at least 5 items.

Then:

* Print the first item.
* Print the last item.
* Add one new item.
* Remove one item.
* Print the updated list.

⸻
"""


items =["books","pens","laptop","phones","cables"]
print(items[0])

print(items[-4])
items.append("Disk")
print(items)


items.remove("pens")
print(items)

# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, 
# and changes made in list1 will automatically also be made in list2.

# You can use the built-in List method copy() to copy a list.

fruits = ["apple","banana","cherry","watermelon"]
fruitslist = fruits.copy()
print(fruitslist)
print(fruits)

# Another way to copy
fruitslist = list(fruits)
print(fruitslist)
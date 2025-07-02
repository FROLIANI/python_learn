
# Lists are used to store multiple items in a single variable.

# for example
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
print(mylist)

# print length of list
print(len(mylist))

mylist = ['apple', 'banana', 'cherry']
print(mylist[1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[4:])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])


thislist = ["blue", "yellow", "green"]
if "yellow" in thislist:
  print("Yes, 'yellow' is in  list")

# Add item
  thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# Remove "banana"
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

  thislist = ["one", "two", "three"]
for i in range(len(thislist)):
    print(thislist[i])


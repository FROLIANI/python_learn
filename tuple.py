
x= ("apple","banana","cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

thistuple = ("test", "testtwo", "three")
for x in thistuple:
  print(x)
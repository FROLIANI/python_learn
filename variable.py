print("Hello First python program")

# The Python print() function is often used to output variables.

x= 5
y= "dev test"

print(x)
print(y)

x=4
x="Python developer"
print(x)

# The Answer is `Python developer`  since at first assigned interger 4 then re-assigned the string
#In python variables are dyamically type, ie can change at run time


# Casting
# If you want to specify the data type of a variable, this can be done with casting.

x = str(3)
y=int(9)
z=float(24)
print(x,y,z)

#Variable names are case-sensitive.
a = 5
A="test case-sensitive"
print(a,A)

# You can also use the + operator to output multiple variables:
x="Today "
y="is "
z="a beautiful day"
print(x + y + z)

# test mathematics
x=5
y=9
print(x+y)

x = 5
y = "testt"
print(x,y) 
print('Hello', 'World')

# Global Variables created outside of  function, used for every one

x = "Python is awesome language"

def testfunc():
  print("desc: " + x) #Identation is required whenever write fuction

testfunc()

# Same variable
x="test value "
def testfunc():
    x = "This is fantastic values"
    print("this is real value: " + x)

testfunc() 
print("Python variable testing: " + x)
#output: Python variable testing: test value

# use the global keyword, the variable belongs to the global scope
def testglobal():
    global x
    x = "fantastic Language"
testglobal()
print("Python is: " + x)
#output: Python is: fantastic Language

# use the global keyword if you want to change a global variable inside a function.
x = "beautiful one"

def testfunc():
    global x
    x = "This is nice ever"
testfunc()
print("real well: " + x)
#output: real well: This is nice ever

# Another sample
x = 'awesome'
def myfunc():
  x = 'fantastic'
myfunc()
print('Python is ' + x)
#output: Python is awesome
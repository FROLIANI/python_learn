# There are three numeric types in Python:
#1. int
#2. float
#3. complex

# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))

# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

# Complex numbers are written with a "j" as the imaginary part:
x = 3 + 5j
y = 5j
z= -5j

print(type(x))
print(type(y))
print(type(z))


# Python has a built-in module called random that can be used to make random numbers:
import random
# The random() function returns a random floating point number N such that 0 <=
print(random.randrange(1,10))
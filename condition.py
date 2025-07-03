
# a= 35
# b = 33
# if b > a:
#    print("b is greater than a")
# elif a == b:
#      print("a and b are equal")
# else:
#     print("a is greater than b")

# ASK user for input number 
# a = int(input("Enter the first Number (a):"))
# b = int(input("Enter the second Number (b):"))

# if b > a:
#     print("b is greater than b")

# elif a == b:
#     print("a and b are equal")
# else:
#     print("a is greater than b")

# a = 35
# numbers = [20, 35, 40, 33, 50]

# for b in numbers:
#     if b > a:
#         print(f"{b} is greater than {a}")
#     elif b == a:
#         print(f"{b} is equal to {a}")
#     else:
#         print(f"{b} is less than {a}")

a = int(input("Enter the target Number (a):"))
input_str = input("Enter a list of numbers separated by comma:")
numbers = [int(x.strip()) for x in input_str.split(",")]

for b in numbers:
    if b > a:
        print(f"{b} is greater than {a}")
    elif b == a:
            print(f"{b} is equal to {a}")
    else:
            print(f"{b} is less than {a}")
           

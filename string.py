
#loop string
for x in "banana":
    print(x)

    # To get the length of a string, use the len() function
    a = "Hello welcome to string python"
    print(len(a))


    # Upper case---modifying string
    a = "Checking UpperCase String"
    print(a.upper())

    # String Concatenation
    a = "test one "
    b = "test two"
    c = a + b
    print(c)

    # Another way
    a = "one"
    b = "two"
    c = a + " " + b
    print(c)

    # Format String
    # age = 26
    # text = "my name is anymnous" + age
    # print(txt)

    # F-String was introduced
    # f ""  {}

    age = 26
    txt = f"my name is anymnous, Iam {age}"
    print(txt)

    x = 'welcome'
    print(x[3])
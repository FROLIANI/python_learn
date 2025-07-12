# Inheritance- Allow us to define class that inherits methods and properties from another class
#parent class ..this is the class being inherited , base class or super class
#child class ..this is the class that inherits from another class, derived class or sub class

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()
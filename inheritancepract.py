class Parent:
    def __init__(self,name):
        self.name = name
    def speak(self):
        print(f"{self.name } says hello")

class Child(Parent):
    def __init__(self, name,age):
        super().__init__(name)
        self.age = age

    def speak(self):
        print(f"{self.name} is {self.age} years old and says hello")


# --- Program Starts Here ---
parent = Parent("Alice")
parent.speak()
child = Child("Bob", 5)
child.speak()   
# Polymorphism allows objects of different classes to be treated using the same interface. In Python,
# this works naturally due to dynamic typing.

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    print(animal.speak())

# Usage
dog = Dog()
cat = Cat()

animal_sound(dog)  # Woof!
animal_sound(cat)  # Meow!

class Father:
    def skills(self):
        print("Gardening and programming")

class Mother:
    def skills(self):
        print("Cooking and painting")

class Child(Father, Mother):
    def skills(self):
        super().skills()
        print("And gaming too")

# Usage
c = Child()
c.skills() 

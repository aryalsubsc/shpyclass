class Mammal:
    def walk(self):
        print("walk")
class Dog(Mammal):
    def bark(self):
        print("Bark")

pet1=Dog()
pet1.bark()

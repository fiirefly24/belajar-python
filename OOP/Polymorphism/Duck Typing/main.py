class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("Woof!")
        
class Cat(Animal):
    def speak(self):
        print("Meow!")
        
class Car:
    alive = False
    
    def speak(self):
        print("Beep! Beep!")
        
animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(f"{animal.alive}")
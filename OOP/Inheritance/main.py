class Animal:
    def __init__(self, name):
        self.name = name
        self.isAlive = True
        
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")
        
class Cat(Animal):
    pass

class Dog(Animal):
    pass

class Mouse(Animal):
    pass

cat = Cat("Tom")
dog = Dog("Dog")
mouse = Mouse("Jerry")

cat.eat()
print(f"{mouse.name} while", end=" ")
dog.sleep()
#inheritanc: allow a class to inherit attributes and methods from other class
#           helps with code reusability & extensibility
#           class chile(Parents)

class Animal:
    def __init__(self, name, is_alive=False):
        self.name = name
        self.is_alive = is_alive

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

#Inheriting Animal class
class Cat(Animal):
    def speak(self):
        print(f"{self.name} speaks meow!")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} speaks bark!")

class cow(Animal):
    def speak(self):
        print(f"{self.name} speaks Moo!")


cat1 = Cat("Scooby")
dog1 = Dog("Nova", True)
cow1 = cow("Moti", True)

cat1.eat()
cat1.speak()
print(cat1.is_alive)

dog1.eat()
dog1.speak()
cow1.speak()
cow1.sleep()

# Polymorphism: greek word means: have many forms
# can be achieved by 2 ways:    
#           1.Inheritance: an object can be treated of same type as parent
#           2."Duck typing": objects must have minimum necessary attributes/methods
#           -----"if it looks like duck, quack like, it must be duck"

# 2.Duck typing
class Animal:
    alive = True
class Dog(Animal):
    def speak(self):
        print("woof!")
    
class Cat(Animal):
    def speak(self):
        print("Meow!")

#Car do not inherit any class
# but it has a method & attributes like Dog & Cat class
class Car:
    alive = False
    def speak(self):
        print("Honk!")

animals = [Dog(), Cat(), Car()]

for animal in animals:
   animal.speak()
   print(animal.alive)
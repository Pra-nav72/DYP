# Multiple inheritance: inherit from more than 1 parent[c(A, B)]

# Multi-level inheritance: inherit from a parent that inherit from another
#   C(B) <- B(A) <- A

class Animal:
    def eat(self):
        print("Animals eat")
    def sleep(self):
        print("Animals sleep")

class Prey(Animal):
    def flee(self):
        print("This animal is fleeing")

class Predator(Animal):
    def hunt(self):
        print("This animal is hunting!")

# multi-level: Rabit <- Prey <- Animal
class Rabit(Prey):
    pass

# multi-level: Lion <- Prey <- Animal
class Lion(Predator):
    pass

# Multiple inheritance
class Fish(Prey, Predator):
    pass


rabit = Rabit()
lion = Lion()
fish = Fish()

rabit.eat() #from parent's parent Animal
rabit.flee() #from parent Prey
# rabit.hunt() #AttributeError: hunt is not rabit's attribute

lion.sleep() #from Parent's Parent Animal
lion.hunt() #from parent Predator

fish.flee() #from 1st parent Prey
fish.hunt() #from 2nd parent Predator
fish.eat() #from patent's parent Animal
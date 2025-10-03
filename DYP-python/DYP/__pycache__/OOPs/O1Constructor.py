# Objects: A "bundle" of related Attributes(variables) &
#           Methods(functions). e.g.phone, cup, books
#   we need class to create many objects.
# 
# Class: a 'Blueprint' used to design structure & layout of an object.
#  
#Methods are acions that are objects can perform
#self refers to object we currently working with
class Car:
    #constructor (__)double underscore--->dunder
    def __init__(self, model, color, year, for_sale):
        #self means this object is createing just now

        #Attributes of class car
        self.model=model
        self.color=color
        self.year=year
        self.for_sale = for_sale

    def drive(self):
        print(f"you drive the {self.color} {self.model}")

    def stop(self):
        print(f"you stop the {self.model}")


def main():
    car1 = Car("BMW", "Blue", 2024, False)
    print(car1)#print only address
    print(car1.model)# '.' is an Attribute access operator
    print(car1.color, car1.year)

    car1.drive()
    car1.stop()

    car2 = Car("Mustang", "Red", 2021, True)
    print(car2.model, car2.color, car2.year, car2.for_sale)
    car2.drive()
    car2.stop()

if __name__ == "__main__":
    main()

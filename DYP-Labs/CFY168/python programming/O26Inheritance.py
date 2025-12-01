class Car:
    def __init__(self,type, year, model):
        self.type = type
        self.year = year
        self.model = model
        print(f"This is an {self.type} car {self.model}")
    
    def disp(self):
        print(f"The {self.model} was manufactured in {self.year}.")

class Audi(Car):
    def __init__(self,type,year, model,  color, engine):
       super().__init__(type, year, model)
       self.color = color
       self.engine = engine

    def details(self):
       print(f"color of {self.model} is {self.color} ")
       print(f"{self.model} has engine {self.engine}")
    
c1 = Car("SUV", 2023, "NEO")
c = Audi("SUV", 2005, "RS Q8 SUV", "red", "V12")
c1.disp()
c.disp()
c.details()
# write a python program to calculate the area of a rectanle using a parameterized constructor
import math
class Shape:
    def __init__(self, type, *args):
        self.type = type
        self.args = args

        self.is_rect = False
        self.is_circle = False

        if len(args) == 3 or len(args) == 2 and type.lower() == 'rectangle' or type.lower() == 'square':
            # print(type, args)
            self.is_rect = True
        elif len(args) == 1 and type.lower() == 'circle':
            # print (type, args)
            self.is_circle = True
        else:
            print(f"enter correct dimensions {args} for {self.type}")


class Rectangle(Shape):
    def __init__(self, type, *args):
        super().__init__(type, *args)
    
    def cal_area_rect(self):
        if self.is_rect:
            return self.args[0] * self.args[1]
        else:
            return "Not a rectangle!"
        
    def cal_peri_rect(self):
        if self.is_rect:
            return 2 * (self.args[0] + self.args[1])
        else:
            return "Not a rectangle!"
    
class Circle(Shape):
    def __init__(self, type, *args):
        super().__init__(type, *args)


    def cal_area_circle(self):
        if self.is_circle:
            x = round(math.pi * self.args[0], 2)
            return x
        else:
            return "Not a circle!"


c = Rectangle("RECtangle", 12, 12)
print(f"area of rectangle: {c.cal_area_rect()}")
print(f"perimeter : {c.cal_peri_rect()}")

c1 = Circle("cirCle", 122)
print(f"area of circle: {c1.cal_area_circle()}")

c = Shape("circle", 12, 13)

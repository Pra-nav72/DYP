import math

#####################Explore: MATH LIBRARY (very useful)##########################

# x=34.5
# y=-23
# z= 4

# print(f"round: {round(x)}")
# print(f"absolute: {abs(x)}") #conver to whole number
# print(f"power: {pow(z, 3)}")    #4 to the power 3
# print(f"maximum: {max(z, y, x)}")
# print(f"minimum: {min(z, y, x)}")

# #using math library
# print(f"value of PI: {math.pi}")
# print(f"value of e: {math.e}")
# print(f"ceil: {math.ceil(x)}") #float to max int value 34.5 --> 35
# print(f"floor: {math.floor(x)}") #34.5--> 34
# print(f"square root: {math.sqrt(z)}") #return type is float


#find circumference and the area of a circle
# radius = float(input("Enter the radius of the circle: "))
# circumference = 2 * math.pi * radius
# area = math.pi * radius * radius

# print(f"circumference: {round(circumference, 2)}")  
# #round(__, 2) to remove extra decimal upto 2 value / round()--> nearest int value
# print(f"area: {round(area, 4)}")



#find the hyptenuse of a triangle
length = float(input("Enter the length of the triangle: "))
height = float(input("Enter the height of the triangle: "))

hypotenuse = math.sqrt((length*length) + (height*height))
print(f"hypotenuse: {hypotenuse}")
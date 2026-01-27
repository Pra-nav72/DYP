# Calculator class
class Calculator:
    def add(self, a, b):
        return a + b

# MathApp class (delegates addition to Calculator)
class MathApp:
    def __init__(self):
        self.calculator = Calculator()   # delegation

    def add(self, a, b):
        return self.calculator.add(a, b)  # delegating the work

# Creating MathApp object
app = MathApp()

# Performing addition using delegation
result = app.add(10, 20)

# Displaying result
print("Addition Result:", result)

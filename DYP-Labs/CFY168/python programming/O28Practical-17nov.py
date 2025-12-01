# WAP to demostrate multiplel inheritance where "smarthphone", subclass inherits from both "phone' and "camera" parent classes.
# allows a subclass to inherit attributes and methods from parent classses. (take suitable properties)

class Phone:
    def __init__(self, model):
        self.model = model
        print(f"model name: {self.model}")

    def call(self, name):
        print(f"call {name}")

class Camera:
    def __init__(self):
        pass
    def click():
        pass

class Smartphone(Phone, Camera):
    pass
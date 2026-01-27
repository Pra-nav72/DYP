class Phone:
    def __init__(self, brand):
        self.brand = brand

    def make_call(self):
        print("Making a phone call...")


class Camera:
    def __init__(self, megapixels):
        self.megapixels = megapixels

    def take_photo(self):
        print(f"Taking a photo with {self.megapixels} MP camera")


class Smartphone(Phone, Camera):
    def __init__(self, brand, megapixels, model):
        Phone.__init__(self, brand)
        Camera.__init__(self, megapixels)
        self.model = model

    def show_details(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Camera: {self.megapixels} MP")



my_phone = Smartphone("Iqoo", 64, "Z9S PRO")


my_phone.make_call()
my_phone.take_photo()
my_phone.show_details()

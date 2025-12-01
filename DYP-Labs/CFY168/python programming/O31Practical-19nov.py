class Car:
    def __init__(self, maker, model, year):
        self.maker = maker
        self.model = model
        self.year = year
        print(f"car {self.model} details registered! \n")

    def display_info(self, id):
        if id in car_details:
            print(f"car manufacturer is : {self.maker}")
            print(f"car model is : {self.model}")
            print(f"year of manufacturing : {self.year}")
        else: 
            print("details not found!")

car_details = {}

while True:
    print("1. Register")
    print("2. get Details")
    print("3. exit")
    n = int(input("number corresponding to function: "))

    if n == 1:

        details=[]

        id = input("Enter id: ")
        maker = input("Enter car maker: ")
        details.append(maker)
        model = input("Enter car model: ")
        details.append(model)
        year = input("Enter year of manufacturing(dd/mm/yyyy): ")
        details.append(details)


        class Child(Car):
            def __init__(self, maker, model, year):
                super().__init__(maker, model, year)


        c = Child(maker, model, year)
        car_details.update({id: details})
        c.display_info(id)

    elif n==2:
        for key, val in car_details.items():
            print("sr.NO. -------maker---------model------year")
            print(f"{key} : {val[0]}")

    elif n==3:
        break

    else:
        print("Not a valid input!")
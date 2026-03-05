class Vehicle:
    def __init__(self, make):
        self.make = make

    def start(self):
        print(f"{self.make} - заводиться.")


class ElectricCar(Vehicle):
    def __init__(self, make, battery_size):
        super().__init__(make)
        self.battery_size = battery_size


    def charge(self):
        print(f"Зараджено батарею ємністю {self.battery_size} kBt")


tesla = ElectricCar("Tesls", 100)
tesla.start()
tesla.charge()



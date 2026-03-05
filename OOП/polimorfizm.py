class Devise:
    def turn_on(self):
        print("Прилад увімкнено.")

class Lamp(Devise):
    def turn_on(self):
        print("Лампа світить яскраво.")

class TV(Devise):
    def turn_on(self):
        print("Телевізор показує новини")


my_devise = [Lamp(), TV()]
for a in my_devise:
    a.turn_on()

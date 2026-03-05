class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def cal_l(self, number):
        print(f"дзвоню на номер {number}, з телефону {self.brand}.")


class SmartPhone(Phone):
    def install_app(self, app_name):
        print(f"Встановлюю додаток {app_name}, на {self.model}")


user2 = SmartPhone("Самсунг", "s105")
user2.cal_l("09-61-231-312")
user2.install_app("Інстаграм")

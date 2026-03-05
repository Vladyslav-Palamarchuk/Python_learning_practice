class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Рахунок поповнено на {amount}, загальна сума {self.balance}.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Недостатньо коштів!")


user1 = BankAccount("Олексій", 2000)
user1.deposit(500)
user1.withdraw(2500)
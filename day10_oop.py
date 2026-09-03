class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"+{amount}. Теперь у {self.owner}: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств!")
        else:
            self.balance = self.balance - amount
            print(f"-{amount}. Осталось: {self.balance}")

    def show(self):
        print(f"{self.owner}: {self.balance} евро")

acc1 = Account("Артём", 500)
acc2 = Account("Катя", 1200)

acc1.show()
acc2.show()

acc1.deposit(300)
acc2.withdraw(100)
acc2.withdraw(9999)

acc2.show()
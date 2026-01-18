class BankAccount:
    def __init__(self, owner, pin, balance=0):
        self.owner = owner
        self.pin = pin
        self.balance = balance

    def check_pin(self, entered_pin):
        return self.pin == entered_pin

    def show_balance(self):
        print("Balans:", self.balance, "so‘m")

    def deposit(self, amount):
        self.balance += amount
        print(amount, "so‘m qo‘shildi")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Yetarli mablag‘ yo‘q")
        else:
            self.balance -= amount
            print(amount, "so‘m yechildi")


account = BankAccount("Jahongir", 1234, 500000)

pin = int(input("PIN kiriting: "))
if account.check_pin(pin):
    while True:
        print("\n1. Balans")
        print("2. Pul qo‘shish")
        print("3. Pul yechish")
        print("0. Chiqish")

        choice = input("Tanlang: ")

        if choice == "1":
            account.show_balance()
        elif choice == "2":
            amount = int(input("Summa: "))
            account.deposit(amount)
        elif choice == "3":
            amount = int(input("Summa: "))
            account.withdraw(amount)
        elif choice == "0":
            print("Xayr!")
            break
        else:
            print("Noto‘g‘ri tanlov")
else:
    print("PIN xato!")

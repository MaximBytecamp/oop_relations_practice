class BankAccount:
    def __init__(self, owner, balance, pin):
        self.owner = owner
        self.__balance = balance
        self.__pin = pin

    def deposit(self, amount):
        pass

    def withdraw(self, amount, pin):
        pass

    def get_balance(self, pin):
        pass

    def change_pin(self, old_pin, new_pin):
        pass


if __name__ == "__main__":
    account = BankAccount("Иван", 5000, "1234")
    account.deposit(1500)
    account.withdraw(1000, "1234")
    print(account.get_balance("1234"))

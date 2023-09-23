class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited {amount} successfully. New balance is {self.__account_balance}."
        else:
            return "Invalid deposit amount. Please enter a positive number."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"Withdrawn {amount} successfully. New balance is {self.__account_balance}."
        elif amount > self.__account_balance:
            return "Insufficient funds for withdrawal."
        else:
            return "Invalid withdrawal amount. Please enter a positive number."

    def display_balance(self):
        return f"Account Balance: {self.__account_balance}"
account = BankAccount("123456789", "John Doe", 1000)
print(account.display_balance())
print(account.deposit(500))
print(account.withdraw(200))
print(account.display_balance())

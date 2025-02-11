from datetime import datetime

class Amount:
    def __init__(self, amount, transaction_type):
        self.amount = amount
        self.timestamp = datetime.now()
        self.transaction_type = transaction_type

    def __str__(self):
        return f'[{self.timestamp}] {self.transaction_type}: ${self.amount:.2f}'

class Account:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(Amount(amount, 'DEPOSIT'))
        print(f'Depositing ${amount:.2f}...')
        print(f'New Balance: ${self.balance:.2f}\n')

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError('Insufficient balance')
        self.balance -= amount
        self.transactions.append(Amount(amount, 'WITHDRAWAL'))
        print(f'Withdrawing ${amount:.2f}...')
        print(f'New Balance: ${self.balance:.2f}\n')

    def transaction_history(self):
        print("Transaction History:")
        for transaction in self.transactions:
            print(transaction)

    def get_balance(self):
        return self.balance

    def get_account_number(self):
        return self.account_number

    def set_account_number(self, account_number):
        self.account_number = account_number

    def get_account_holder(self):
        return self.account_holder

    def set_account_holder(self, account_holder):
        self.account_holder = account_holder

    def __str__(self):
        return f'Account Holder: {self.account_holder}\nAccount Number: {self.account_number}\nCurrent Balance: ${self.balance:.2f}\n'

    def __add__(self, other):
        return self.balance + other.balance

    def __sub__(self, other):
        return self.balance - other.balance

account = Account('12345678', 'John Doe')

print(account)

account.deposit(500)

account.withdraw(200)

account.transaction_history()
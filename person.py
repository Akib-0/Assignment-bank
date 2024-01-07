from datetime import datetime
class Person:
    def __init__(self,name) -> None:
        self.name = name

class User(Person):
    def __init__(self, name, bank) -> None:
        super().__init__(name)
        self.balance = 0
        self.bank = bank

    def deposite(self,amount):
        self.balance += amount
        self.bank.total_balance += amount
        print(f'{self.name} deposied {amount} tk')
        transection = f'{datetime.now()}: {self.name} deposited {amount} tk'
        self.update_transection_history(transection)

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            self.bank.total_balance -= amount
            print(f'{self.name} withdrawed {amount} tk')
            transection = f'{datetime.now()}: {self.name} withdrawed {amount} tk'
            self.update_transection_history(transection)
        else:
            print("NOT ENOUGH MONEY")

    def transfer(self,amount,user):
        if self.balance >= amount:
            self.balance -= amount
            user.balance += amount
            print(f'{self.name} tranferred {amount} tk to {user.name}')
            transection = f'{datetime.now()}: {self.name} tranferred {amount} tk to {user.name}'
            self.update_transection_history(transection)
        else:
            print("Not enough money")

    def take_loan(self,amount):
        if not self.bank.loan:
            print("Sorry loan feature is currently disabled")
        else:
            max_loan = 2*self.balance
            if self.balance <= max_loan:
                self.balance += amount
                self.bank.total_loan_taken += amount
                self.bank.total_balance += amount
                print(f'{datetime.now()}: {self.name} succesfully taken {amount} tk loan.')
            else:
                print("Sorry you can take the loan right now")

    def update_transection_history(self, transection):
        if self.name not in self.bank.transections:
            self.bank.transections[self.name] = []
        self.bank.transections[self.name].append(transection)

    def transection_history(self):
        if self.name in self.bank.transections:
            print("Transaction History:")
            for transaction in self.bank.transections[self.name]:
                print(transaction)
        else:
            print("No transactions found for this user.")

        

class Admin(Person):
    def __init__(self, name,bank) -> None:
        super().__init__(name)
        self.bank = bank

    def total_bank_balance(self):
        print("Total Balance: ",self.bank.total_balance)

    def total_loan(self):
        print(f'Users taken total {self.bank.total_loan_taken} tk from the bank')

    def loan_feature(self,feature):
        self.bank.loan = feature


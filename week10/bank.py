class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def __repr__(self):
        return str(self.__dict__)



class Account:
    accountnumber = 0
    def __init__(self, accountNumber, name, balance=0):
        self.accountNumber = accountNumber+1
        self.name = name
        self.balance = balance
        self.customers = {}

    def __repr__(self):
        return str(self.__dict__)

class Customer:
    def __init__(self, *args):
        if len(args) == 1:
            self.name = args[0] 
        if len(args) == 2:
            self.name = args[0] 
            self.cpr = args[1]
            
    def __repr__(self):
        return str(self.__dict__)

class DanskeBank:
    pass

bank = Bank("Den Helt Dyre")
customer1 = Customer("Dabmaster 5000", "1337-420-69")
account1 = Account("1", customer1)
bank.accounts[customer1] = account1

customer2 = Customer("Freddy Licious", "12349-1241")
account2 = Account("2", customer1)
bank.accounts[customer2] = account2

print(bank.accounts)
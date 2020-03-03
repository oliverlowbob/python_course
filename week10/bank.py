class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def __repr__(self):
        return str(self.__dict__)

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.customers = {}

    def __repr__(self):
        return str(self.__dict__)

class Customer:
    def __inint__(self, *args):
        if len(args) == 1:
            self.name = args[0] 
        if len(args) == 2:
            self.name = args[0] 
            self.cpr = args[1]
            
    def __repr__(self):
        return str(self.__dict__)
        
class DanskeBank:
    pass
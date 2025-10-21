# Bank Management System 
class BankAccount: 
    def __init__(self, account_holder, initial_balance=0): 
        self.account_holder = account_holder 
        self.balance = initial_balance 
        self.transaction_history = [] 

from bank import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, interest):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.interest = interest

    def apply_interest(self):
        interest = self.current_balance * self.interest
        self.current_balance += interest
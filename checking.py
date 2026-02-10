from bank import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, transfer_limit):
        super().__init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.transfer_limit = transfer_limit
        self.transfers_made = 0

    def transfer(self, transfer_amount):
        if self.transfers_made >= self.transfer_limit:
            print("Transfer limit reached.")
            return
        self.withdraw(transfer_amount)
        self.transfers_made += 1

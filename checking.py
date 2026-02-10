from bank import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.transfer_limit = transfer_limit
        self.transfers_made = 0

    def transfer(self, transfer_amount):
        # withdraws transfer amount from checking account
        # if successful, balance updates and transfers made increases
        # if it fails, transfers made stays the same

        if self.transfers_made >= self.transfer_limit:
            print("Transfer limit reached.")
            return

        before = self.current_balance

        self.withdraw(transfer_amount)

        if self.current_balance == before:
            print("Transfer failed.")
            return

        self.transfers_made += 1
        print("Transfer successful.")

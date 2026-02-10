class BankAccount:
    bank_title = "Bank"

    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self._account_number = account_number
        self.__routing_number = routing_number

    def deposit(self, deposit_amount):
        self.current_balance += deposit_amount
        print(f"Successfully deposited {deposit_amount}.")
        print(f"Current balance: {self.current_balance}")

    def withdraw(self, withdraw_amount):
        if self.current_balance - withdraw_amount < self.minimum_balance:
            print(f"Cannot withdraw less than minimum balance of {self.minimum_balance}.")
            print(f"Current balance: {self.current_balance}")
        else:
            self.current_balance -= withdraw_amount
            print(f"Successfully withdrawn {withdraw_amount}")
            print(f"Current balance: {self.current_balance}")

    def print_customer_information(self):
        print(f"Bank Title: {self.bank_title}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Current Balance: {self.current_balance}")

class SavingsAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, interest):
        super().__init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.interest = interest

    def apply_interest(self):
        interest = self.current_balance * self.interest
        self.current_balance += interest

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



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


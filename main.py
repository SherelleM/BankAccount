from savings import SavingsAccount
from checking import CheckingAccount

s1 = SavingsAccount("Mary Jane", 500, 25, "12345", "123456", 0.05)
s2 = SavingsAccount("Billy Joe", 1000, 100, "23456", "234567", 0.075)

# Mary deposits 500, tries to withdraw 1000 but is under balance,
# so then withdraws 200, then applies interest, which would be 840, print info
s1.deposit(500)
s1.withdraw(1000)
s1.withdraw(200)
s1.apply_interest()
s1.print_customer_information()


# Billy withdraws 500, deposits 2000, tries to withdraw 2600 but cant,
# then applies interest, should be 2687.5, print info
s2.withdraw(500)
s2.deposit(2000)
s2.withdraw(2600)
s2.apply_interest()
s2.print_customer_information()


c1 = CheckingAccount("Mary Jane", 500, 25, "01234", "012345", 2)
c2 = CheckingAccount("Billy Joe", 1000, 100, "34567", "345678", 4)

# Mary deposits 500, then transfers out 500,
# tries to transfer 600 but is under balance so transfers 400, then tries to transfer
# 50 but transfer limit reached so final balance is 100, print info
c1.deposit(500)
c1.transfer(500)
c1.transfer(600)
c1.transfer(400)
c1.transfer(50)
c1.print_customer_information()


# Billy withdraws 500, deposits 2000, tries to transfer 2500 but its under min balance,
# so transfers 250, then transfers 250, then transfers 250, then transfers 250
# then tries to transfer 250 but reached transfer limit so current balance is 1500, print info
c2.withdraw(500)
c2.deposit(2000)
c2.transfer(2500)
c2.transfer(250)
c2.transfer(250)
c2.transfer(250)
c2.transfer(250)
c2.transfer(250)
c2.print_customer_information()
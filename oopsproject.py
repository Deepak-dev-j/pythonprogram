from bank_account import *

a=BankAccount(1000,"suniyo")
b=BankAccount(2000,"nobit")

a.get_Balance()
b.get_Balance()

a.deposit(500)
b.deposit(200)

a.withdraw(100)

a.transfer(200,b)

mani=IntrestRewardedAcct(100,"mani")
mani.get_Balance()
mani.deposit(100)

kani=IntrestRewardedAcct(100,"kani")
kani.get_Balance()
kani.withdraw(100)
kani.transfer(5,a)



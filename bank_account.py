class BalanceException(Exception):
    pass
class BankAccount:
    def __init__(self,Initial_amount,accnt_name):
        self.balance=Initial_amount
        self.name=accnt_name

        print(f"\naccount {self.name} created.\nBalance=${self.balance:2f}")

        # balance check

    def get_Balance(self):
        print(f"\nAccount {self.name} \nBalance={self.balance:2f}")

        # deposit the money

    def deposit(self,amount):
        self.balance=self.balance+amount

        print("Deposit complete")
        self.get_Balance()
#    withdraw method

    def viable_transaction(self,amount):
        if self.balance>=amount:
            return
        else:
            raise BalanceException(f"\n Sorry,account {self.name} only has balance of {self.balance}")
            
     

    def withdraw(self,amount):
        try:
            self.viable_transaction(amount)
            self.balance=self.balance-amount
            print("wihtdraw complete")
        except BalanceException as error:
            print(f"\n  Withdraw intruppted :{error}")
    

    # tranfer money

    def transfer(self,amount,account):
        try:
            print("************\n Begining Transfer....🐌\n************")
            self.viable_transaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("Transefer completed.....")
        except  BalanceException as error:
            print(f"\n Transefer INtrupted {error}")


# rewrd the account
class IntrestRewardedAcct(BankAccount):
        def deposit(self, amount):
           self.balance=self.balance+(amount*1.05)
           print("\n Deposit completed....")
           self.get_Balance()

class savingAcct(IntrestRewardedAcct):
    def __init__(self, Initial_amount, accnt_name):
        super().__init__(Initial_amount, accnt_name)
        self.fee=5

    def withdraw(self,amount):
        try:
            self.viable_transaction(amount+self.fee)
            self.balance=self.balance-(amount+self.fee)
            print("\n Withdraw completed ..")
            self.get_Balance()
        except BalanceException as error:
            print(f"\n Withdraw intruppted :{error}")
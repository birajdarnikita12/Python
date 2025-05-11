# Create Account class with 2 attributes - balance & account no. 
# Create methods for debit, credit and printing the balance.

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
    
    # Debit method
    def debit(self, amount):
        print("RS." , amount,"is debited")
        self.balance-=amount
        print("Total balance =", self.get_balance())
    
    # Credit Method
    def credit(self, amount):
        self.balance+=amount
        print("RS." , amount,"is credit")
        print("Total balance =", self.get_balance())

    # Balance method
    def get_balance(self):
        return self.balance
 
acc1 = Account(10000, 12345)
'''print(acc1.balance)
print(acc1.account_no)'''
acc1.debit(500)
acc1.credit(1000)
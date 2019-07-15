class BankAccount:
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate
        

    def __str__(self):
        return f"You're balance is {self.balance}"

    def deposit(self, amount):
        self.balance =+ amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def gain_interest(self):
        rate = self.interest_rate / 100
        interest_total = rate * self.balance
        self.balance += interest_total 

        return self.balance


chequing = BankAccount(100, 49)
# print(chequing)

# print(chequing.deposit(100)

print(chequing.gain_interest())
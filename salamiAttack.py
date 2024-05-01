import time

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

# Simulating a salami attack by making multiple small deposits
account_number = '123456789'
account = BankAccount(account_number)

for _ in range(100):  # Simulate 100 small deposits
    amount = 0.01  # Small deposit amount
    account.deposit(amount)
    time.sleep(0.1)  # Sleep for 0.1 seconds between each deposit

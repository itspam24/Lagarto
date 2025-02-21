class BankAccount:
    def __init__(self, account_number, owner, balance=0.0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
           self.balance += amount
           print(f"Deposited ₱{amount:.2f}. New balance: ₱{self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
               self.balance -= amount
               print(f"Withdraw ₱{amount:.2f}. New balance: ₱{self.balance:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def display_balance(self):
        print(f"Account Balance for {self.owner} (Account #{self.account_number}): ₱{self.balance:.2f}")


if __name__ == "__main__":
    account = BankAccount(account_number="10082305", owner="Hera Ai", balance=3000.0)

    account.display_balance()
    account.deposit(2000.0)
    account.withdraw(300.0)
    account.withdraw(200.0)
    account.display_balance()

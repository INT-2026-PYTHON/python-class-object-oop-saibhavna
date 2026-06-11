"""
## 2. Bank Account Class  *(Medium)*

=================================================
BANK ACCOUNT CLASS
=================================================

Problem Statement:
Write a Python CLASS called `BankAccount`
that represents a simple bank account. Each
account has an account holder's name, a
unique account number, and a balance that
starts at 0 unless an opening balance is
given.

The class must support deposits, withdrawals,
and balance checks. Reject invalid operations
(negative amounts, overdrafts) by printing a
clear message — do NOT crash.

-------------------------------------------------
Instructions:
1. Define a class:
      class BankAccount:
2. Constructor:
      def __init__(self, name, account_number,
                   opening_balance=0):
          - validate that opening_balance >= 0
          - store name, account_number, balance
            on `self`
3. Instance methods:
      - deposit(self, amount)
            * reject amount <= 0 with a message
            * otherwise add to balance
      - withdraw(self, amount)
            * reject amount <= 0
            * reject if amount > balance
            * otherwise subtract from balance
      - get_balance(self)
            * return the current balance
      - __str__(self)
            * return a friendly string like:
              "Account[001 - Alice]: $500"
4. In the driver code:
      - create AT LEAST TWO accounts
      - perform some valid deposits / withdraws
      - perform AT LEAST ONE invalid operation
        (negative amount or overdraft) on each
        account to show the rejection message
      - print each account using print(acc),
        which triggers __str__
5. Do NOT use:
   - class-level mutable defaults (e.g. a list
     as default argument)
   - global variables

-------------------------------------------------
Input Example:
a1 = BankAccount("Alice", "001", 500)
a2 = BankAccount("Bob",   "002")
a1.deposit(200)
a1.withdraw(100)
a1.withdraw(2000)   # overdraft -> rejected
a2.deposit(-50)     # invalid   -> rejected
a2.deposit(300)

Output Example:
Insufficient funds for Alice (balance=600, asked=2000)
Deposit amount must be > 0 (got -50)
Account[001 - Alice]: $600
Account[002 - Bob]:   $300

-------------------------------------------------
Explanation:
- `self.balance` is independent for every
  object, so Alice and Bob keep separate
  balances.
- Validation in `deposit` and `withdraw` shows
  how methods use `self` to read AND update
  state on the same object.
- `__str__` returns the human-readable form
  used by print().
=================================================

"""

class BankAccount:
    def __init__(self, name, account_number, opening_balance=0):
        if opening_balance < 0:
            print("Opening balance cannot be negative. Setting balance to 0.")
            opening_balance = 0

        self.name = name
        self.account_number = account_number
        self.balance = opening_balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount.")
        else:
            self.balance += amount
            print(f"Deposited ₹{amount}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            print("Insufficient funds. Withdrawal rejected.")
        else:
            self.balance -= amount
            print(f"Withdrawn ₹{amount}")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account[{self.account_number} - {self.name}]: ₹{self.balance}"



name1 = input("Enter first account holder name: ")
acc1 = input("Enter first account number: ")
bal1 = float(input("Enter opening balance: "))

name2 = input("Enter second account holder name: ")
acc2 = input("Enter second account number: ")
bal2 = float(input("Enter opening balance: "))

a1 = BankAccount(name1, acc1, bal1)
a2 = BankAccount(name2, acc2, bal2)

dep1 = float(input("Enter deposit amount for first account: "))
a1.deposit(dep1)

with1 = float(input("Enter withdrawal amount for first account: "))
a1.withdraw(with1)


dep2 = float(input("Enter deposit amount for second account: "))
a2.deposit(dep2)

with2 = float(input("Enter withdrawal amount for second account: "))
a2.withdraw(with2)


print("\nAccount Details:")
print(a1)
print(a2)

print("\nBalances:")
print(a1.name, "Balance =", a1.get_balance())
print(a2.name, "Balance =", a2.get_balance())
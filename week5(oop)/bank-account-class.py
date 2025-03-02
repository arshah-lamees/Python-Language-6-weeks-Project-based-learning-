class BankAccount:#parent class
    def __init__(self, account_number, balance=0):
        self._account_number = account_number
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. New balance: ${self._balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self._balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        return self._balance

    def display_info(self):
        print(f"Account Number: {self._account_number}")
        print(f"Current Balance: ${self._balance}")


class SavingsAccount(BankAccount):#child class
    def __init__(self, account_number, balance=0, interest_rate=0.02):
        super().__init__(account_number, balance)
        #super().__init__(account_number, balance)is used to inheret all methods of parent class, 'Person.__init__(self, account_number, balance )' is used to inheret specified parent method
        self._interest_rate = interest_rate

    def add_interest(self):
        interest = self._balance * self._interest_rate
        self.deposit(interest)
        # print(f"Added interest: ${interest:.2f}")
        return interest

    def display_info(self):
        super().display_info()
        interest = self.add_interest()
        print(f"Interest Rate: {self._interest_rate * 100}%")
        print(f"Projected Balance with Interest: ${self._balance + interest:.2f}")

class CheckingAccount(BankAccount):#child class
    def __init__(self, account_number, balance=0, overdraft_limit=100):
        super().__init__(account_number, balance)
        self._overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0 and self._balance + self._overdraft_limit >= amount:
            self._balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self._balance}")
        else:
            print("Invalid withdrawal amount or overdraft limit exceeded.")

    def display_info(self):
        super().display_info()
        print(f"Overdraft Limit: ${self._overdraft_limit}")


def main():
    print("Welcome to the Bank Account Management System")
    while True:
        account_type = input("Enter account type (S for Savings, C for Checking): ").upper()
        if account_type not in ['S', 'C']:
            print("Invalid choice. Please try again.")
        else:
            account_number = input("Enter account number: ")
            initial_balance = float(input("Enter initial balance: $"))
            break 

    if account_type == 'S' :
        account = SavingsAccount(account_number, initial_balance, interest_rate=0.02)
    elif account_type == 'C':
        account = CheckingAccount(account_number, initial_balance, overdraft_limit=100)

    while True:
        print("\nChoose an operation:\n")
        print("1. Display Account Info")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        # if account_type == 'S' :
        #     print("5. Add Interest")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            account.display_info()
        elif choice == '2':
            amount = float(input("Enter deposit amount: $"))
            account.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter withdrawal amount: $"))
            account.withdraw(amount)
        elif choice == '4':
            print(f"Current balance: ${account.get_balance()}")
        elif choice == '5' and account_type == 'S':
            account.add_interest()
        elif choice == '6':
            print("Thank you for using our banking system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()

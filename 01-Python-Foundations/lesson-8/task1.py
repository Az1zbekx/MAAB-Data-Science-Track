import os

class BankAccount:
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be positive.")
            return
        self.balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def display_balance(self):
        print(f"{self.name}'s current balance: ${self.balance:.2f}")

    def save(self):
        with open(f"{self.name}.txt", "w") as file:
            file.write(str(self.balance))

    @staticmethod
    def load(name):
        if os.path.exists(f"{name}.txt"):
            with open(f"{name}.txt", "r") as file:
                balance = float(file.read())
            return BankAccount(name, balance)
        else:
            return BankAccount(name)


# Command-line loop
def main():
    name = input("Enter your name: ")
    account = BankAccount.load(name)

    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            try:
                amt = float(input("Enter amount to deposit: "))
                account.deposit(amt)
            except ValueError:
                print("Invalid amount.")
        elif choice == "2":
            try:
                amt = float(input("Enter amount to withdraw: "))
                account.withdraw(amt)
            except ValueError:
                print("Invalid amount.")
        elif choice == "3":
            account.display_balance()
        elif choice == "4":
            account.save()
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

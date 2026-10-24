import os

class Account:
    def __init__(self, account_number, name, balance=0.0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount

    def to_line(self):
        return f"{self.account_number},{self.name},{self.balance}\n"

    @staticmethod
    def from_line(line):
        acc_num, name, balance = line.strip().split(",")
        return Account(acc_num, name, float(balance))


class Bank:
    def __init__(self):
        self.accounts = {}
        self.filename = "accounts.txt"
        self.load_from_file()

    def generate_account_number(self):
        return str(len(self.accounts) + 1).zfill(6)  # e.g., 000001

    def create_account(self, name, initial_deposit):
        if initial_deposit < 0:
            raise ValueError("Initial deposit must be non-negative.")
        acc_num = self.generate_account_number()
        account = Account(acc_num, name, initial_deposit)
        self.accounts[acc_num] = account
        self.save_to_file()
        print(f"✅ Account created! Account Number: {acc_num}")

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if not account:
            raise KeyError("❌ Account not found.")
        print("\n--- Account Details ---")
        print(f"Account Number: {account.account_number}")
        print(f"Name: {account.name}")
        print(f"Balance: ${account.balance:.2f}")

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if not account:
            raise KeyError("❌ Account not found.")
        account.deposit(amount)
        self.save_to_file()
        print("✅ Deposit successful.")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if not account:
            raise KeyError("❌ Account not found.")
        account.withdraw(amount)
        self.save_to_file()
        print("✅ Withdrawal successful.")

    def save_to_file(self):
        with open(self.filename, "w") as f:
            for account in self.accounts.values():
                f.write(account.to_line())

    def load_from_file(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                for line in f:
                    account = Account.from_line(line)
                    self.accounts[account.account_number] = account


# === CLI Interface ===
def main():
    bank = Bank()

    while True:
        print("\n=== BANK MENU ===")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                name = input("Enter your name: ")
                initial = float(input("Initial deposit: $"))
                bank.create_account(name, initial)

            elif choice == "2":
                acc_num = input("Enter account number: ")
                bank.view_account(acc_num)

            elif choice == "3":
                acc_num = input("Enter account number: ")
                amount = float(input("Amount to deposit: $"))
                bank.deposit(acc_num, amount)

            elif choice == "4":
                acc_num = input("Enter account number: ")
                amount = float(input("Amount to withdraw: $"))
                bank.withdraw(acc_num, amount)

            elif choice == "5":
                print("👋 Goodbye!")
                break

            else:
                print("❗ Invalid choice. Try again.")

        except ValueError as ve:
            print("❌ Error:", ve)
        except KeyError as ke:
            print("❌ Error:", ke)


if __name__ == "__main__":
    main()

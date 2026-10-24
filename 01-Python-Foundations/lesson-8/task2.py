import uuid
import json
import os

class Account:
    def __init__(self, account_number, name, balance=0.0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("✅ Mablag' manfiy yoki nol bo'lishi mumkin emas.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("✅ Mablag' manfiy yoki nol bo'lishi mumkin emas.")
        if amount > self.balance:
            raise ValueError("❌ Hisobda yetarli mablag' mavjud emas.")
        self.balance -= amount

    def to_dict(self):
        return {
            "account_number": self.account_number,
            "name": self.name,
            "balance": self.balance
        }

    @staticmethod
    def from_dict(data):
        return Account(
            data["account_number"],
            data["name"],
            data["balance"]
        )


class Bank:
    def __init__(self):
        self.accounts = {}
        self.file = "accounts.json"
        self.load_from_file()

    def generate_account_number(self):
        return str(uuid.uuid4())

    def create_account(self, name, initial_deposit):
        if initial_deposit < 0:
            raise ValueError("Boshlang'ich depozit manfiy bo'lishi mumkin emas.")
        account_number = self.generate_account_number()
        account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = account
        self.save_to_file()
        print(f"✅ Hisob yaratildi. Hisob raqami: {account_number}")

    def get_account(self, account_number):
        if account_number not in self.accounts:
            raise KeyError("❌ Bunday hisob topilmadi.")
        return self.accounts[account_number]

    def view_account(self, account_number):
        acc = self.get_account(account_number)
        print("\n--- HISOB MA'LUMOTLARI ---")
        print(f"Hisob raqami: {acc.account_number}")
        print(f"Ism: {acc.name}")
        print(f"Balans: ${acc.balance:.2f}")

    def deposit(self, account_number, amount):
        acc = self.get_account(account_number)
        acc.deposit(amount)
        self.save_to_file()
        print("✅ Depozit muvaffaqiyatli amalga oshirildi.")

    def withdraw(self, account_number, amount):
        acc = self.get_account(account_number)
        acc.withdraw(amount)
        self.save_to_file()
        print("✅ Mablag' yechib olindi.")

    def save_to_file(self):
        try:
            data = {acc_num: acc.to_dict() for acc_num, acc in self.accounts.items()}
            with open(self.file, "w") as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print("❌ Faylni saqlashda xatolik:", e)

    def load_from_file(self):
        if not os.path.exists(self.file):
            return
        try:
            with open(self.file, "r") as f:
                data = json.load(f)
                self.accounts = {acc_num: Account.from_dict(acc_data)
                                 for acc_num, acc_data in data.items()}
        except Exception as e:
            print("❌ Faylni yuklashda xatolik:", e)


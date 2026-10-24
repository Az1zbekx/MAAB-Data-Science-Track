def main():
    bank = Bank()

    while True:
        print("\n====== BANK MENUSI ======")
        print("1. Hisob yaratish")
        print("2. Hisobni ko'rish")
        print("3. Depozit kiritish")
        print("4. Pul yechish")
        print("5. Chiqish")
        print("=========================")

        choice = input("Tanlovingiz (1-5): ")

        try:
            if choice == "1":
                name = input("Ismingizni kiriting: ")
                deposit = float(input("Boshlang'ich depozit: $"))
                bank.create_account(name, deposit)

            elif choice == "2":
                acc_num = input("Hisob raqamingizni kiriting: ")
                bank.view_account(acc_num)

            elif choice == "3":
                acc_num = input("Hisob raqami: ")
                amount = float(input("Depozit miqdori: $"))
                bank.deposit(acc_num, amount)

            elif choice == "4":
                acc_num = input("Hisob raqami: ")
                amount = float(input("Yechiladigan miqdor: $"))
                bank.withdraw(acc_num, amount)

            elif choice == "5":
                print("👋 Dasturdan chiqildi.")
                break

            else:
                print("❗ Noto'g'ri tanlov.")

        except ValueError as ve:
            print("⚠️ Xato:", ve)
        except KeyError as ke:
            print("⚠️ Xato:", ke)
        except Exception as e:
            print("⚠️ Noma'lum xatolik:", e)


if __name__ == "__main__":
    main()

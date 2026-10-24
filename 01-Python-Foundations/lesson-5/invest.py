def invest(amount, rate, years):
    for i in range(1, years + 1):
        amount += (amount * rate) / 100
        print(f"year {i}: ${amount:.2f}")
try:
    amount = float(input("Amount = "))
    rate = float(input("Rate = "))
    years = int(input("Years = "))
    
    if amount < 0 or rate < 0 or years < 0:
        print("Error")
    else:
        invest(amount, rate, years)

except ValueError:
    print("Error")
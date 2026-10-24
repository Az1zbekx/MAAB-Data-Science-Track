password = input("Password = ")
if len(password) < 8:
    print("Password is too short.")
else:
    if any(c.isupper() for c in password):
        print("Password is strong.")
    else:    
        print("Password must contain an uppercase letter.")
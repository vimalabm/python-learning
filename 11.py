#11. banking application

balance=90000
withdrawlamount=float(input("Withdrawl amount="))

if balance>=withdrawlamount:
    balance=balance-withdrawlamount
    print("balance=", balance)
else:
    print("Insufficient balance")

print(type(balance))

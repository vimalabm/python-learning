#13. ATM withdrawal system

balance=float(input("Balance="))
withdrawalamount=int(input("Withdrawal amount="))

remainingbalance= balance - withdrawalamount

if balance>=withdrawalamount and withdrawalamount>0 and remainingbalance>=500:
    print("Withdrawal amount=", withdrawalamount)
    print("Remaining balance=", remainingbalance)
else:
    print("Withdrawal not allowed")
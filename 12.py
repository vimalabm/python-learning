#12. shopping checkout system

productprice=float(input("Product price="))
quantity=int(input("Quantity="))
discountpercentage=float(input("Discount percentage="))

total= productprice * quantity
discountamount= total * discountpercentage / 100
finalamount= total - discountamount
print("Final amount=", finalamount)

if finalamount>=5000:
    print("Free premiuim delivery")
else:
    print("Standard delivery")
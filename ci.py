principal=int(input("enter principal amount "))
rate=int(input("enter rate of intrest "))
time=int(input("enter time in year "))
amount=(principal*((1+ rate)/100))**time
print("amount ",amount)
ci=amount-principal
print("compound intrest ",ci)

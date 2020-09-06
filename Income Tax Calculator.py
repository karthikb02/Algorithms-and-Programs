amount=int(input())
if amount<=250000:
    print("0.00")
elif amount<=500000:
    balance=amount-250000
    tax=(balance*5)/100
    print("%.2f"%tax)
elif amount<=1000000:
    balance=amount-500000
    tax=12500+(balance*20)/100
    print("%.2f"%tax)
else:
    balance=amount-1000000
    tax=12500+100000+(balance*30)/100
    print("%.2f"%tax)

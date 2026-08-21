#input product name, qty, rate to display productname, amount, discount, Taxable amount, VAT, Net amount?
ProductName=(input("Enter ProductName:"))
qty=float(input("Enter Quantity:"))
rate=float(input("Enter Rate:"))
discount=str(input("Enter Discount:"))
amount=qty*rate
discount=amount*5/100
taxableamount=amount-discount
vat=taxableamount*13/100
netamount=taxableamount+vat
print("ProductName",ProductName)
print("Quantity",qty)
print("Rate",rate)
print("Discount",discount)
print("Amount",amount)
print("taxableamount",taxableamount)
print("vat",vat)
print("netamount",netamount)
print("thanks for choosing us")
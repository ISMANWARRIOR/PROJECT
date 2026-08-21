#WAP to input previous unit and current unit to find out consume unit, payable amount, vat and net amount?
pu=float(input("Previous Unit:"))
cu=float(input("Consume Unit:"))
totalunit=cu-pu
if totalunit<20:
    payableamount=100
    print("Payable Amount:",payableamount)
else:
    payableamount=(totalunit-20)*6.5+100
    print("Payable Amount:",payableamount)
    vat=payableamount*4/100
    Netamount=payableamount+vat
    print("Vat:",vat)
    print("Net amount:",Netamount)

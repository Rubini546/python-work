service=int(input('plz select:'))
if service==1:
    print('withdraw')
    amount=int(input("Enter a amount:"))
    pin=int(input("Enter your a secret pin:"))
if  pin==PIN:
                  print('collect your amount',amount)
                  run=false
else:
    print('incorrect pin')
    run=true

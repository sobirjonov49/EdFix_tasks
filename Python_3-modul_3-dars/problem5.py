# Qoldiqli bo'lishga tekshirish

a=int(input("a="))
b=int(input("b="))

if a>b and a%b==0:
    print('True')
elif b>=a and b%a==0:
    print('True')
else:
    print('False')
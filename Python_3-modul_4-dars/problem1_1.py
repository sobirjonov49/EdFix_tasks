a=int(input('N='))
k=0
while a>0:
    k=k*10+a%10   
    a=a//10
print(k)
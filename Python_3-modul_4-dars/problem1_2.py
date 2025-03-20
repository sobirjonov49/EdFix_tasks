lst1=[]
print('Enter the numbers:')
for i in range(10):
    lst1.append(int(input()))
print(lst1)
k=0
m=1
for i in range(10):
    if lst1[i]%2==0:
        k+=lst1[i]
    else:
        m*=lst1[i]
print('Odds:', k)
print('Evens:', m)
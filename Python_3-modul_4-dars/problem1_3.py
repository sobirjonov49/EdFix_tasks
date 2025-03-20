from random import randint
lst1=[]
lst1=[randint(0,9) for i in range(10)]
print(lst1)

k=0
j=0  
for i in range(10):
    if lst1[i]==i:
        print('True')
        k+=1
    else:
        print('False')
        j+=1
print('True:', k)
print('False:', j)
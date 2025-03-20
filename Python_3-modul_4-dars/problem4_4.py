from random import randint
tublar=[]
lst1=[randint(2,100) for i in range(20)]
print('list1:',lst1)

for i in range(20):
    k=0
    for j in range(2,lst1[i]):
        if lst1[i]%j==0:
            k+=1
    if k==0:
        tublar.append(lst1[i])
print('tublar:',tublar)


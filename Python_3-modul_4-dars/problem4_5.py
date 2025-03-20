from random import randint

lst1=[randint(1,100) for i in range(20)]

print(lst1)
lst2=[]
lst3=[]
for i in range(10):
    lst2.append(lst1[i])
    lst2.sort()
print(lst2)
for i in range(10, 20):
    lst3.append(lst1[i])
    lst3.sort(reverse=True)
print(lst3)
print(lst2+lst3)
lst2.extend(lst3)
print(lst2)
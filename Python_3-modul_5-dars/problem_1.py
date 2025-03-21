#ikki listni ketma ketlikda birlashtirish dasturi 
from random import randint
len1=randint(2,9)
len2=randint(2,9)
print("len1=",len1)
print("len2=",len2)

list1=[randint(1,50) for _ in range(len1)]
list2=[randint(1,50) for _ in range(len2)]
print(list1)
print(list2)

list3=[]
for a, b in zip(list1, list2):
    list3.append(a)
    list3.append(b)
    
min_len=min(len1, len2)
if len1>len2:
    list3.extend(list1[min_len:])
elif len2>len1:
    list3.extend(list2[min_len:])


print("New list:",list3)
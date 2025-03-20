from random import randint

set1={randint(1,50) for i in range(10)}
set2={randint(1,50) for i in range(10)}
umumiy=set1.intersection(set2)

print(set1)
print(set2)
print(umumiy)
print("Sum_umumiy:", sum(umumiy))
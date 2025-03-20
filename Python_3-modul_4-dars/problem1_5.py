from random import randint

list=[randint(1, 100) for i in range(5)]
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)

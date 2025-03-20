from random import randint
n=int(input('How many numbers do you want to enter? '))
lst=[randint(0,5) for i in range(n)]
print(lst)
sum_index=0
sum_value=0
for i in range(n):
    sum_index+=i
    sum_value+=lst[i]

if sum_index==sum_value:
    print("WOW")
if sum_index>sum_value:
    print("INDEX")
if sum_index<sum_value:
    print('VALUE')
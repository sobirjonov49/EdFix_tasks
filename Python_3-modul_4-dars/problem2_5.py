from random import randint

nums=[randint(1,10) for i in range(10)]
a=int(input("Enter a number "))
k=0
for i in range(10):
    if nums[i]==a:
        k+=1
print(nums)
print("Number", a, " have", k, "times in list")
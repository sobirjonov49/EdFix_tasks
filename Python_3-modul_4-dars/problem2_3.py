from random import randint

nums=[randint(1, 100) for i in range(20)]
print(nums)
sum=0
for i in range(20):
    sum+=nums[i]
print(sum)
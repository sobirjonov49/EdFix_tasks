from random import randint

nums=[randint(1, 100) for i in range(20)]
print(nums)

yegindi=sum(nums)
nums.append(f"SUM: {yegindi}")
print(nums)


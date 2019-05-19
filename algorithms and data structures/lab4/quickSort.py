import random

def quickSort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
        left = [elem for elem in nums if elem > q]

        middle = [q] * nums.count(q)
        right = [elem for elem in nums if elem < q]
        return quickSort(left) + middle + quickSort(right)

sorted = [1, 2, 4, 6, 7, 8, 10, 13, 46, 56, 68, 98]
reversed = quickSort(sorted)
print(reversed)
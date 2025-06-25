def rob(nums):
    prev1, prev2 = 0, 0
    for num in nums:
        current = max(prev1, prev2 + num)
        prev2, prev1 = prev1, current
    return prev1

myarr = [2, 7, 9, 3, 1]
print(rob(myarr))
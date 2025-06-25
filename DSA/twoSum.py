
def twoSum(nums, target):
    numToIndex = {}
    for i, num in enumerate(nums):
        if target - num in numToIndex:
            return numToIndex[target - num], i
        numToIndex[num] = i

array = [2, 7, 11, 15]
print(twoSum(array,9))
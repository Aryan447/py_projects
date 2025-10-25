from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        bestSum = float('-inf')
        # bestSum = nums[0] # this can also be used instead of float('-inf')
        currentSum = 0

        for num in nums:
            currentSum = max(num, currentSum + num)
            bestSum = max(currentSum, bestSum)

        return int(bestSum)


mySol = Solution()

nums = [-2,1,-3,4,-1,2,1,-5,4] # 6

print(mySol.maxSubArray(nums))

from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        if len(cost) == 1:
            return cost[0]
        n = len(cost)

        minCost = [0] * n
        minCost[0] = cost[0]
        minCost[1] = cost[1]

        for i in range(2, n):
            minCost[i] = cost[i] + min(minCost[i-1], minCost[i-2])
        return min(minCost[-1], minCost[-2])

mysol = Solution()

print(mysol.minCostClimbingStairs([1, 100,1,1,1,100,1,1,100,1]))

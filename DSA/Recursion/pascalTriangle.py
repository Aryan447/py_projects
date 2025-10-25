'''
Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:

Input: numRows = 1
Output: [[1]]

'''

from typing import List, Optional

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]

        prevRows = self.generate(numRows-1)
        prevRow = prevRows[-1]
        currentRow = [1]

        for i in range(1, numRows-1):
            currentRow.append(prevRow[i-1] + prevRow[i])

        currentRow.append(1)
        prevRows.append(currentRow)

        return prevRows


mysol = Solution()
print(mysol.generate(5))

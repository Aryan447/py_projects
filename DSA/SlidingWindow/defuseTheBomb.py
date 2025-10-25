'''

'''

from typing import List
import unittest

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * 4

        for i in range(0, len(code)-1):


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test1(self):
        self.assertEqual(self.solution.decrypt(code = [5,7,1,4], k = 3), [12,10,16,13])

    def test2(self):
        self.assertEqual(self.solution.decrypt(code = [1,2,3,4], k = 0), [0,0,0,0])

    def test3(self):
        self.assertEqual(self.solution.decrypt(code = [2,4,9,3], k = -2), [12, 5, 6, 13])

if __name__ == '__main__':
    unittest.main()

mySol = Solution()


from typing import List, Optional
import unittest

class Solution:
    def maxDifference(self, s: str) -> int:


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test1(self):
        self.assertEqual(self.solution.maxDifference("aaaaabbc"), 3)
    def test2(self):
        self.assertEqual(self.solution.maxDifference("abcabcab"), 1)

if __name__ == '__main__':
    unittest.main()

from typing import List, Optional

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reverseWords = []

        for word in range(len(words)-1, -1, -1):
            reverseWords.append(words[word])

        return " ".join(reverseWords)


mysol = Solution()
print(mysol.reverseWords("the quick brown fox"))

# 문제: https://leetcode.com/problems/valid-anagram/
# 해설: https://www.algodale.com/problems/valid-anagram/
# 위치: https://github.com/DaleStudy/leetcode-study/tree/main/valid-anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      return sorted(s) == sorted(t)


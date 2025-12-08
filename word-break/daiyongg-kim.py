""" Failed Attempt
 class Solution:
     def wordBreak(self, s: str, wordDict: List[str]) -> bool:

         for word in wordDict:
             if word in s:
                 s = s.replace(word, '')
             else:
                 return False
         return len(s) == 0
"""
class Solution:
     def wordBreak(self, s: str, wordDict: List[str]) -> bool:

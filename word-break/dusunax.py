'''
# 139. Word Break

use dynamic programming to check if the string is segmentable.

> **use dp to avoid redundant computations:**
> backtracking approach will check all possible combinations of words recursively, which has time complexity of O(2^n))

## Time and Space Complexity

```
TC: O(n^2)
SC: O(n)
```

#### TC is O(n^2):
- nested loops for checking if the string is segmentable. = O(n^2)
  - outer loop: iterate each char index from the start to the end. = O(n)
  - inner loop: for each index in the outer loop, checks substrings within the range of valid words in wordDict. = worst case, O(n)

#### SC is O(n):
- using a dp array to store whether index i is segmentable. = O(n)
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)

        segment_dp = [False] * (n + 1) # SC: O(n)
        segment_dp[0] = True # Base case: an empty string is segmentable

        for end in range(1, n + 1): # TC: O(n^2)
            for start in range(end):
                if segment_dp[start] and s[start:end] in word_set:
                    segment_dp[end] = True
                    break
        
        return segment_dp[n]

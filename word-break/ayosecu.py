from typing import List

class Solution:
    """
        - Time Complexity: O(n^2), n = len(s)
        - Space Complexity: O(n + m)
            - n = len(s) = dp size
            - m = The number of characters in wordDict (wordDict size)
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordDict = set(wordDict)

        # Use DP: dp[i] => s[0:i] is possible to be seperated by dictionary words
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break   # s[i-1] is possible => don't need to check forward string
        
        return dp[-1]   # check s[0:n]

tc = [
        ("leetcode", ["leet","code"], True),
        ("applepenapple", ["apple","pen"], True),
        ("catsandog", ["cats","dog","sand","and","cat"], False)
]

sol = Solution()
for i, (s, wordDict, e) in enumerate(tc, 1):
    r = sol.wordBreak(s, wordDict)
    print(f"TC {i} is Passed!" if r == e else f"TC {i} is Failed! - Expected: {e}, Result: {r}")

"""
    TC: O(n)
    SC: O(n)

    DNF, read solutions by Dale...ㅠㅠ
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {len(s): 1}

        def dfs(start):
            if start in memo:
                return memo[start]

            if s[start] == "0":
                return 0
            if start + 1 < len(s) and int(s[start: start+2]) < 27:
                memo[start] = dfs(start + 1) + dfs(start + 2)
            else:
                memo[start] = dfs(start + 1)
            return memo[start]

        return dfs(0)

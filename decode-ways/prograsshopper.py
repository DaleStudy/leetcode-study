class Solution:
    def numDecodings(self, s: str) -> int:
        # sol 1: Time complexity O(n)
        dp = {len(s): 1}

        def dfs(start):
            if start in dp:
                return dp[start]
            if s[start] == "0":
                return 0
            result = None
            if start + 1 < len(s) and int(s[start:start+2]) < 27:
                result = dfs(start+1) + dfs(start+2)
            else:
                result = dfs(start+1)
            dp[start] = result
            return result

        return dfs(0)

# idea : Tree
class Solution:
    def numDecodings(self, s: str) -> int:
        # recurisve : top-down
        # DP : bottom-up can be another way to solve it, but it is not clear for me. 
        memo = {len(s):1}
        def dfs(start):
            if start in memo:
                return memo[start]
            if s[start] == '0':
                memo[start] = 0
            elif start+1 < len(s) and int(s[start:start+2]) < 27:
                memo[start] = dfs(start+1) + dfs(start+2)
            else:
                memo[start] = dfs(start+1)
            return memo[start]
        return dfs(0)



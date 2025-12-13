"""
Blind75 - Decode Ways
https://leetcode.com/problems/decode-ways/
시간복잡도: O(n)
공간복잡도: O(n)
풀이 : 메모이제이션 + DFS를 활용한 재귀 풀이

아..DP로는 못 풀겠어서 풀이 봤습니다. 강의나 책을 봐야겠군요
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s) + [1]
        for start in reversed(range(len(s))):
            if s[start] == "0":
                dp[start] = 0
            elif start + 1 < len(s) and int(s[start : start + 2]) < 27:
                dp[start] = dp[start + 1] + dp[start + 2]
            else:
                dp[start] = dp[start + 1]
        return dp[0]
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {len(s): 1}

        def dfs(start):
            if start in memo:
                return memo[start]

            if s[start] == "0":
                memo[start] = 0
            elif start + 1 < len(s) and int(s[start : start + 2]) < 27:
                memo[start] = dfs(start + 1) + dfs(start + 2)
            else:
                memo[start] = dfs(start + 1)
            return memo[start]

        return dfs(0)



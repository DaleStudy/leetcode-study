"""
Time complexity O(n)
Space complexity O(1)

Dynamic programming
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        n = len(s)
        if n == 1:
            return 1
        tmp = int(s[:2])
        dp = [1, 1]
        if 11 <= tmp <= 26:
            if tmp != 20:
                dp = [1, 2]
        elif s[1] == '0':
            if tmp not in [10, 20]:
                return 0
        if n == 2:
            return dp[-1]
        
        for i in range(2, n):
            if s[i] == '0':
                if s[i-1] in ['1', '2']:
                    cur = dp[0]
                else:
                    return 0
            else:
                cur = dp[1]
                tmp = int(s[i-1:i+1])
                if (11 <= tmp <= 26) and (tmp != 20):
                    cur += dp[0]
            dp = [dp[1], cur]

        return dp[-1]

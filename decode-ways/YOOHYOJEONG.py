# https://leetcode.com/problems/decode-ways

class Solution(object):
    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        
        # dp[i] = i번째까지 문자열을 해석하는 방법의 개수
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, n + 1):
            # 1자리 체크
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            
            # 2자리 체크
            two_digit = int(s[i-2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2]
        
        return dp[n]

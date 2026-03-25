# idea
# 마지막 두자리 수가 독립 가능 -> dp[i] = dp[i-1] + dp[i-2]
#   마지막 한자리 수가 독립 가능 -> dp[i] = dp[i-1]
#     위 두 케이스 모두 불가능 -> 0 반환
# TC : O(n)
# SC : O(n)

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [1] * len(s)

        if s[0] == '0':
            return 0
        
        if '1' <= s[0] and s[0] <= '9':
            dp[0] = 1

        for i in range(1, len(s)):
            target = s[i-1:i+1]
            
            if int(s[i]) != 0 and 10 <= int(target) and int(target) <= 26:
                dp[i] = dp[i-1] + dp[i-2]
                continue

            if int(s[i]) == 0 and 10 <= int(target) and int(target) <= 26:
               dp[i] = dp[i-2]
               continue

            target = s[i]
            if 1 <= int(target) and int(target) <= 9:
                dp[i] = dp[i-1]
                continue

            return 0
        
        return dp[len(s) - 1]

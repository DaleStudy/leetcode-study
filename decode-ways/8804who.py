class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0]*(len(s)+1)
        s = '0'+s
        dp[0] = 1
        for i in range(1, len(s)):
            if int(s[i]) == 0:
                if int(s[i-1]) != 1 and int(s[i-1]) != 2:
                    return 0 
                else:
                    dp[i]=dp[i-2]
            elif int(s[i]) <= 6:
                if int(s[i-1]) != 1 and int(s[i-1]) != 2:
                    dp[i]=dp[i-1]
                else:
                    dp[i]=dp[i-1]+dp[i-2]
            else:
                if int(s[i-1]) == 1:
                    dp[i]=dp[i-1]+dp[i-2]
                else:
                    dp[i]=dp[i-1]
        return dp[-1]
    

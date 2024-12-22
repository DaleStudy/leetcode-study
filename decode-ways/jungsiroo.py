class Solution:
    def numDecodings(self, s: str) -> int:
        """
        dp 이용 : 가능한 경우의 수를 구해놓고 그 뒤에 붙을 수 있는가?
        ex) 1234
            (1,2) -> (1,2,3)
            (12) -> (12,3)
            (1) -> (1,23)
		
		Tc : O(n) / Sc : O(n)
        """
        if s[0] == '0': return 0

        n = len(s)
        dp = [0]*(n+1)
        dp[0] = dp[1] = 1

        for i in range(2, n+1):
            one = int(s[i-1])
            two = int(s[i-2:i])

            if 1<=one<=9: dp[i] += dp[i-1]
            if 10<=two<=26 : dp[i] += dp[i-2]

        return dp[n]
        

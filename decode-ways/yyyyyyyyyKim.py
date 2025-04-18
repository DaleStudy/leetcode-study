class Solution:
    def numDecodings(self, s: str) -> int:
        
        # DP
        dp = [0]*(len(s)+1)

        # s가 0으로 시작하면 0 return
        if s[0] == '0':
            return 0

        dp[0] = 1   # 빈문자열은 해석가능한 1가지 경우로 취급 (초기기준점 역할, dp[i-2]계산시필요)
        dp[1] = 1   # 첫번째자리의 처리방법은 1가지

        # len(s)가 2 이상일때
        for i in range(2,len(s)+1):
            one = int(s[i-1])   # 한자리(현재자리)
            two = int(s[i-2:i]) # 한자리 + 앞자리 = 두자리

            if 1 <= one <= 9:
                dp[i] += dp[i-1]
            if 10 <= two <= 26:
                dp[i] += dp[i-2]

        return dp[len(s)]

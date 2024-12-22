class Solution:
    def numDecodings(self, s: str) -> int:
        dp = []
        if (s[0] == '0'):
            return 0
        dp.append(1)

        for idx, _ in enumerate(s):
            if idx == 0:
                continue
            if s[idx] == '0':
                if s[idx-1] == '1' or s[idx-1] == '2':
                    if idx == 1:
                        dp.append(1)
                    else:
                        dp.append(dp[idx-2])
                else:
                    return 0
            elif s[idx-1] == '1' or (s[idx-1] == '2' and (s[idx] >= '1' and s[idx] <= '6')):
                if idx == 1:
                    dp.append(2)
                else:
                    dp.append(dp[idx-1] + dp[idx-2])
            else:
                dp.append(dp[idx-1])

        return dp[-1]


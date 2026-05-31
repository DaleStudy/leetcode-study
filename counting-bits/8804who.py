import math

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0, 1]
        num = 1
        idx = 2

        while idx <= n:
            num *= 2
            temp = idx+(num//2)
            temp2 = temp+(num//2)

            for i in range(idx, temp):
                dp.append(dp[i-(num//2)])
                idx += 1
            for i in range(temp,temp2):
                dp.append(dp[i-(num//2)]+1)
                idx += 1
        
        return dp[:n+1]
    

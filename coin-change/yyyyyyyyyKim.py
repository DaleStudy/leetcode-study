class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # DP
        dp = [10001]*(amount+1)
        dp[0] = 0

        # 1부터 amount까지 만들 수 있는 최소 동전의 수를 dp에 업데이트
        for i in range(1, amount+1):
            for j in coins:
                # dp[i-j]+1 : (i-j)원을 만드는 최소 동전 수 + 현재동전(j) 1개 사용
                # 현재금액(i)를 만들 수 있는 최소 동전 수 업데이트
                if i - j >= 0:
                    dp[i] = min(dp[i], dp[i-j]+1)
            
        # 업데이트된 값이 없으면 -1 리턴
        if dp[amount] == 10001:
            return -1
        else:
            return dp[amount]

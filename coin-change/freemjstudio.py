class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        INF = int(1e9)
        # dp[n] 은 n 원을 만들기 위한 최소한의 동전 개수를 저장한다.
        dp = [INF] * (amount + 1)
        usable_coins = []
        for coin in coins:
            if coin == amount:
                return 1
            if coin < amount:
                dp[coin] = 1 # dp[3] = 1
                usable_coins.append(coin)

        # dp 를 채워나가는 과정
        for i in range(1, amount+1):
            for coin in usable_coins:
                if (i - coin) >= 0 and dp[i - coin] != INF:
                    dp[i] = min(dp[i - coin] + 1, dp[i])

        return -1 if dp[amount] == INF else dp[amount]

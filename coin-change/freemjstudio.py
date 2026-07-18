class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [0] * (amount + 1) # dp[n] 은 n 원을 만들기 위한 최소한의 동전 개수를 저장한다.

        for coin in coins:
            if coin == amount:
                return 1
            if coin < amount:
                dp[coin] = 1

        # dp 를 채우자
        for i in range(amount)

        return dp[amount] if dp[amount] != 0 else -1

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        result = [amount + 1] * (amount + 1)
        result[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i >= c:
                    result[i] = min(result[i], result[i - c] + 1)

        if result[amount] == amount + 1:
            return -1

        return result[amount]

        ## TC: O(n * len(coins)) , SC: O(n), where n denotes amount

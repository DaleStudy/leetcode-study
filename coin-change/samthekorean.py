# a is number of amount and c is number of coins
# TC : O(a∗c)
# SC: O(a)
class Solution:
    def coinChange(self, denominations: List[int], target_amount: int) -> int:
        minimum_coins = [target_amount + 1] * (target_amount + 1)
        minimum_coins[0] = 0

        for current_amount in range(1, target_amount + 1):
            for coin in denominations:
                if current_amount - coin >= 0:
                    minimum_coins[current_amount] = min(
                        minimum_coins[current_amount],
                        1 + minimum_coins[current_amount - coin],
                    )

        return minimum_coins[-1] if minimum_coins[-1] != target_amount + 1 else -1

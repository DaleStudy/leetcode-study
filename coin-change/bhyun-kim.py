"""
322. Coin Change
https://leetcode.com/problems/coin-change/

Solution: Dynamic Programming
    To solve this problem, we can use dynamic programming.
    We can define a dp array to store the minimum number of coins needed to make up the amount.
    We can iterate through the coins and the amount to update the dp array.
    The minimum number of coins needed to make up the amount is the minimum of the current dp value and the dp value at the previous amount minus the current coin value plus one.
    
    - Initialize a dp array with length amount + 1 and set dp[0] to 0.
    - Iterate through the coins and the amount to update the dp array.
    - Return dp[amount] if it is less than or equal to the amount, otherwise return -1.

Time complexity: O(n * m)
    - n is the amount.
    - m is the number of coins.
    - We iterate through the coins and the amount to update the dp array.

Space complexity: O(n)  
    - We use a dp array of length amount + 1 to store the minimum number of coins needed to make up each amount.
"""

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # Base case

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != amount + 1 else -1

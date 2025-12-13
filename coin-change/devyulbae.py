"""
Blind 75 - Coin Change
LeetCode Problem Link: https://leetcode.com/problems/coin-change/
시간복잡도 : O(n*m) (n: amount, m: len(coins))
공간복잡도 : O(n)

"""
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins: # 각 동전마다
            for x in range(coin, amount + 1): # 금액 1 coin부터 amount까지
                dp[x] = min(dp[x], dp[x - coin] + 1) # 해당 금액을 만들기 위한 최소 동전 개수 갱신

        return dp[amount] if dp[amount] != float('inf') else -1 # amount를 만들 수 없는 경우 -1 반환
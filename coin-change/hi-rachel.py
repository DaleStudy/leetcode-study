
# BFS -> 먼저 찾는 해답이 가장 적은 연산/가장 짧은 거리 -> 가장 적은 count부터 계산해 최소한의 동전 수 보장
# O(amount * n) time, O(amount) space

from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        queue = deque([(0, 0)])  # (동전 개수, 현재 금액)
        visited = set()
        while queue:
            count, total = queue.popleft()
            if total == amount:
                return count
            if total in visited:
                continue
            visited.add(total)
            for coin in coins:
                if total + coin <= amount:
                    queue.append((count + 1, total + coin))
        return - 1
    

# DP 풀이
# 어떤 금액을 만드는데 필요한 동전 개수를 알면, 그 금액보다 큰 금액을 만드는데 필요한 동전 개수도 알 수 있다.
# dp[i] = min(dp[i], dp[i - coin] + 1)
# O(amount * n) time, O(amount) space

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [amount + 1] * amount

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] < amount + 1 else -1

# idea: DFS/BFS, DP

from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Why Greedy is not possiple way?
        # A greedy is only optimal in specific coin systems (e.g., denominations like 1, 5, 10, 25)
        # For arbitrary coin denominations, a greedy approach does not always yield the optimal solution.
        queue = deque([(0,0)]) # (동전갯수, 누적금액)
        while queue:
            count, total = queue.popleft()
            if total == amount:
                return count
            for coin in coins:
                if total + coin <= amount:
                    queue.append([count+1, total+ coin])
        return -1

    # # BFS 
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     queue = deque([(0,0)]) # (동전갯수, 누적금액)
    #     visited = set()
    #     while queue:
    #         count, total = queue.popleft()
    #         if total == amount:
    #             return count
    #         if total in visited:
    #             continue
    #         visited.add(total)
    #         for coin in coins:
    #             if total + coin <= amount:
    #                 queue.append([count+1, total+ coin])
    #     return -1


    # DP
    # dp[i] = min(dp[i], dp[i-coin]+1)
    # from collections import deque
    # class Solution:
    #     def coinChange(self, coins: List[int], amount: int) -> int:
    #        dp=[0]+[amount+1]*amount
    #        for coin in coins:
    #             for i in range(coin, amount+1):
    #                 dp[i] = min(dp[i], dp[i-coin]+1)
    #         return dp[amount] if dp[amount] < amount else -1



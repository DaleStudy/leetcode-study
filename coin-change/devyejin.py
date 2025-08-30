# # 중복조합
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#
#         def backtrack(current, total):
#             if total == amount:
#                 return len(current)
#
#             if total > amount:
#                 return float('inf')
#
#             min_count = float('inf')
#             for coin in coins:
#                 current.append(coin)
#                 result = backtrack(current, total + coin)
#                 min_count = min(min_count, result)
#                 current.pop()
#
#             return min_count
#
#         ans = backtrack([], 0)
#         return -1 if ans == float('inf') else ans
from collections import deque
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        queue = deque([(0, 0)])
        visited = set([0])

        while queue:
            current_amount, count = queue.popleft()

            for coin in coins:
                new_amount = current_amount + coin
                if new_amount == amount:
                    return count + 1
                if new_amount < amount and new_amount not in visited:
                    visited.add(new_amount)
                    queue.append((new_amount, count + 1))

        return -1


from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        queue = deque([(0, 0)])
        vis = set()

        while queue:
            total, count = queue.popleft()
            if total == amount:
                return count
            for coin in coins:
                nxt = total + coin
                if nxt > amount:
                    continue
                if nxt in vis:
                    continue
                vis.add(nxt)
                queue.append((nxt, count + 1))
        return -1

# TC: O(amount * len(coins))
# SC: O(amount)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        from collections import deque

        v = {0: 0}
        q = deque([0])

        while q and amount not in v:

            cur = q.popleft()

            for coin in coins:

                if cur + coin > amount or cur + coin in v:
                    continue

                v[cur + coin] = v[cur] + 1
                q.append(cur + coin)

        return -1 if amount not in v else v[amount]


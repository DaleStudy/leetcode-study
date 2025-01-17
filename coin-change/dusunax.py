'''
# 322. Coin Change

use a queue for BFS & iterate through the coins and check the amount is down to 0.
use a set to the visited check.

## Time and Space Complexity

```
TC: O(n * Amount)
SC: O(Amount)
```

#### TC is O(n * Amount):
- sorting the coins = O(n log n)
- reversing the coins = O(n)
- iterating through the queue = O(Amount)
- iterating through the coins and check the remaining amount is down to 0 = O(n)

#### SC is O(Amount):
- using a queue to store (the remaining amount, the count of coins) tuple = O(Amount)
- using a set to store the visited check = O(Amount)
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if len(coins) == 1 and coins[0] == amount:
            return 1

        coins.sort() # TC: O(n log n)
        coins.reverse() # TC: O(n)
        
        queue = deque([(amount, 0)]) # SC: O(Amount)
        visited = set() # SC: O(Amount)

        while queue: # TC: O(Amount)
            remain, count = queue.popleft()

            for coin in coins: # TC: O(n)
                next_remain = remain - coin

                if next_remain == 0:
                    return count + 1
                if next_remain > 0 and next_remain not in visited:
                    queue.append((next_remain, count + 1))
                    visited.add(next_remain)
    
        return -1

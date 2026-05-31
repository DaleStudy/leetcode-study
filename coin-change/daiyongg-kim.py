class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        level = [0]
        visited = {0}
        count = 0

        while level:
            count += 1
            next_level = []

            for current_amount in level:
                for coin in coins:
                    new_amount = current_amount + coin

                    if new_amount == amount:
                        return count
                    
                    if new_amount < amount and new_amount not in visited:
                        visited.add(new_amount)
                        next_level.append(new_amount)
            level = next_level

        return -1

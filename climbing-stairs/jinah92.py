# 공간복잡도: O(1), 시간복잡도: O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        
        prev, curr  = 1, 2
        for num in range(3, n+1):
            prev, curr = curr, prev + curr
        
        return curr

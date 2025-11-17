class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        prev, curr = 1, 2 

        for i in range(3, n+1):
            next = prev + curr
            prev = curr
            curr = next
        
        return curr
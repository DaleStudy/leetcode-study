# 시간복잡도 : O(n), 공간복잡도 : O(1)

class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 2
        if (n == 1):
            return 1
        elif (n == 2):
            return 2
        for i in range(n - 2):
            c = a
            a = b
            b = c + b
        return (b)
    

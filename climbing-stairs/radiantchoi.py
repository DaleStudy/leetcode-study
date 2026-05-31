class Solution:
    def climbStairs(self, n: int) -> int:
        stairs = [1, 1]

        if n > 1:
            for i in range(2, n+1):
                stairs.append(stairs[i - 1] + stairs[i - 2])
        
        return stairs[-1]

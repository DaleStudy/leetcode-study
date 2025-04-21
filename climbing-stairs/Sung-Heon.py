class Solution:
    def climbStairs(self, n: int) -> int:
        temp = {}
        if n == 1:
            return 1
        if n == 2:
            return 2
        temp[1] = 1
        temp[2] = 2
        a = 2
        while a != n:
            a += 1
            temp[a] = temp[a - 1] + temp[a - 2]
        return temp[a]


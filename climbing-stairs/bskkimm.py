class Solution:
    def __init__(self):
        self.memo = {}
    
    def climbStairs(self, n: int) -> int:
        
        # n = 3 --> 3: 111, 2: 12, 21: --> 3
        # n = 4 --> 4: 1111, 3: 112, 121, 211, 2: 22 --> 5
        # n = 5 --< 5: 11111,4: 1112, 1121, 1211, 2111, 3: 221, 212, 122, --> 8
        # n = 6 --> 6: 111111, 5: 5, 4: 2211, 1122, 1221, 2112, 1212, 2121, 3: 1 --> 13

        # a(n+2) = a(n+1) + a(n)

        if n == 1:
            return 1
        elif n == 2:
            return 2

        if n in self.memo: # need to return when memo is available w.r.t n
            return self.memo[n]

        self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.memo[n]

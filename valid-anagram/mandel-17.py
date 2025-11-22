import collections

class Solution:
    num_dict = collections.defaultdict(int)

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        if self.num_dict[n]:
            return self.num_dict[n]
        
        self.num_dict[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.num_dict[n]

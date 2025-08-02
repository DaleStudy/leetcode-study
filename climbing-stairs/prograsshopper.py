class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        sol 1
        Runtime: Beats 100.00% / O(n^2)
        Memory: Beats 8.16% / O(1)
        '''
        import math
        ways = 1
        max_count_2steps = int(n/2)
        for i in range(1, max_count_2steps+1):
            current = math.perm(n - i) / (math.perm(i) * math.perm(n-(2*i)))
            ways += current
        return int(ways)

        '''
        sol 2
        Runtime: Beats 100.00% / O(n^2)
        Memory: Beats 48.54% / O(1)
        '''
        ways = 0
        max_count_2steps = n // 2
        for i in range(max_count_2steps + 1):
            ways += math.comb(n - i, i)
        return ways

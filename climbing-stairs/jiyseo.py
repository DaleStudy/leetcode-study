class Solution(object):
    def fac(self, n) :
        fac = 1
        for i in range(1, n + 1) :
            fac *= i
        return fac

    def climbStairs(self, n):
        res = 0
        for i in range(n // 2 + 1) :
            if i == 0 :
                res += 1
            else :
                cnt = n - i
                res += Solution().fac(cnt)/(Solution().fac(i) * Solution().fac(cnt - i))
        return res
        

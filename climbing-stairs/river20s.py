class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        f(n)이 계단을 올라갈 수 있는 방법의 수라면,
        f(n) = f(n-1) + f(n-2)

        """
        # 기저 조건:
        # n이 1인 경우 1 반환
        if n == 1:
            return 1
        # n이 2인 경우 2 반환
        if n == 2:
            return 2
        # 재귀 호출 
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

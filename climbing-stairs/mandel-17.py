class Solution:
    def climbStairs(self, n: int) -> int:
        def factorial(n):
            result = 1
            for i in range(1, n+1):
                result *= i
            return result

        def combination(n, r):
            top = factorial(n)
            bottom = factorial(n-r) * factorial(r)
            return top / bottom

        share = n // 2
        total = 1
        for i in range(1, share + 1):
            combination_n = n - i
            combination_r = i

            total += combination(combination_n, combination_r)

        return int(total)
    
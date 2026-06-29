# class Solution:
#     def climbStairs(self, n: int) -> int:
#         """
#             O(N) with additional space
#         """
#         if n <= 2:
#             return n

#         dp = [0] * (n + 1)
#         dp[1] = 1
#         dp[2] = 2

#         for i in range(3, n + 1):
#             dp[i] = dp[i - 1] + dp[i - 2]

#         return dp[-1]

# class Solution:
#     """
#         O(N) Found that solution is fibonacci number
#     """
#     def climbStairs(self, n: int) -> int:
#         if n <= 2:
#             return n

#         p1, p2 = 1, 2
#         for i in range(3, n + 1):
#             p1, p2 = p2, p1 + p2

#         return p2


# Fibonacci hack
class Solution:
    def climbStairs(self, n: int) -> int:
        """
            O(Log N)
        """

        # O(1) operation
        def mat_mul(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
            ans = [[0] * 2 for _ in range(2)]

            for i in range(2):
                for j in range(2):
                    for k in range(2):
                        ans[i][j] += a[i][k] * b[k][j]

            return ans

        # O(Log N) operation
        def mat_pow(a: List[List[int]], n: int) -> List[List[int]]:
            if n == 1:
                return [[1, 1], [1, 0]]

            half = mat_pow(a, n // 2)
            multed = mat_mul(half, half)

            if n % 2:
                return mat_mul(multed, [[1, 1], [1, 0]])
            else:
                return multed

        ans = mat_pow([[1, 1], [1, 0]], n)

        return ans[0][0]

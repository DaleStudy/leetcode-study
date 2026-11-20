class Solution:
    # 풀이3) Bottom-up DP 
    # 사실상 피보나치 수열: dp[n] = dp[n-1] + dp[n-2]
    # 시간 복잡도: O(n), 공간 복잡도: O(1)
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        first, second = 1, 2          # 1번째, 2번째 계단 오르는 방법 수
        for i in range(3, n + 1):
            first, second = second, first + second
        return second


# 풀이2) Top-down DP (재귀 & 메모이제이션)
# 시간 복잡도: O(n) 
# 공간 복잡도: O(n)
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         dp = [0] * (n + 1)
#
#         def climb(n):
#             if dp[n] != 0:      
#                 return dp[n]
#             if n <= 2:          # 초기 세팅
#                 dp[n] = n
#             else:
#                 dp[n] = climb(n - 1) + climb(n - 2)
#             return dp[n]
#
#         return climb(n)


# 풀이1) Bottom-up DP (배열) - Time: O(n), Space: O(n)
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         # dp로 접근
#         dp=[0]*(n+1)
#         for i in range(1,n+1):
#             if i==1:
#                 dp[i]=1
#             elif i==2:
#                 dp[i]=2
#             else:
#                 dp[i]=dp[i-1]+dp[i-2]
#         return dp[n]


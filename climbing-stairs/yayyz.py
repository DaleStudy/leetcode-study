"""
📝 Problem: LeetCode 70 - Climbing Stairs
📅 Date: 2025-04-07

🚀 Approach:
- Bottom-up DP using an array
- dp[i] = dp[i-1] + dp[i-2]

⏱️ Time Complexity: O(n)
💾 Space Complexity: O(n)

📌 Notes:
- Base case: dp[0] = 1, dp[1] = 1
- dp[i]: i번째 계단으로 도달하기 위한 모든 경우의 수를 가짐 
- n <= 2의 경우는 f(1) + f(0)이 합해진 경우이기 때문에 n을 반환
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: 
            return n
        dp = [0] * (n + 1) # n 번째의 계단을 오르는 방법을 찾기 위해 dp배열 생성
        dp[0] = 1
        dp[1] = 1
        # n번째의 계단을 오르기 위해서는 
        # n-1, n-2번째의 계단에서 올수있는 경우의 수들의 합이 n번째 계단을 오르기 위한 모든 경우의 수
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

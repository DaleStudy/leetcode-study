# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        """
        [Complexity]
            - TC: O(n)
            - SC: O(1)

        [Approach]
            dp[i] = i-th step을 오를 때, 가능한 distinct ways의 수
                  = dp[i - 1] + dp[i - 2]
            이때, dp[i - 1]과 dp[i - 2]만 필요하므로, O(1) space로 optimize 가능하다.
                prev1 = dp[i - 1]
                prev2 = dp[i - 2]
            첫 번째 계단을 오르는 방법에는 1개가 있으므로, 초깃값은 다음과 같이 설정할 수 있다.
                prev1 = 1
                prev2 = 0
        """

        prev1, prev2 = 1, 0
        for _ in range(n):
            prev1, prev2 = prev1 + prev2, prev1
        return prev1

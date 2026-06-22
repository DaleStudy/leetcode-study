class Solution:
    def climbStairs(self, n: int) -> int:
        """
        n번째 계단에 도달하는 서로 다른 방법의 수를 구한다.
        한 번에 1칸 또는 2칸씩 올라갈 수 있으므로 DP를 사용하여 dp[i] = dp[i-1] + dp[i-2] 점화식을 사용한다.
        시간복잡도 O(n), 계단을 한 번 순회하며 결과를 계산한다.
        """
        dp = [0] * (n + 2)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

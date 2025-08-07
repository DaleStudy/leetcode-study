class Solution:
    """
        1일 때, 1 step -> 1개
        2일 때, 1 + 1, 2 -> 2개
        3일 때, 1 + 1 + 1, 1 + 2, 2 + 1 -> 3개
        4일 때, 1 + 1 + 1 + 1, 1 + 1 + 2, 1 + 2 + 1, 2 + 1 + 1, 2 + 2 -> 5개
        5일 때, 1 + 1 + 1 + 1 + 1, 1 + 1 + 1 + 2, 1 + 1 + 2 + 1, 1 + 2 + 1 + 1, 2 + 1 + 1 + 1, 1 + 2 + 2, 2 + 1 + 2, 2 + 2 + 1 -> 8개
        순서대로 봤을 때, 이전 값과 그 이전 값의 합이 현재 개수이다.
        이를 점화식으로 봤을 때, dp[i] = d[i - 1] + dp[i - 2]가 된다.

        - Time Complexity: O(n)
            - 1부터 n까지 한 번씩 반복하므로 선형 시간
        - Space Complexity: O(n)
            - dp 배열에 n개의 값을 저장하므로 선형 공간 사용
    """
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return n

        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]

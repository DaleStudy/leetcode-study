class Solution {
    public int climbStairs(int n) {
        // n=1일때 방법은 1가지다.
        // n=2일때 방법은 2가지다.
        // n=3일때 방법은 3가지다.
        // n=4일때 방법은 5가지다.
        // 1,1,1,1
        // 1,1,2
        // 1,2,1
        // 2,1,1
        // 2,2
        // dp 알고리즘으로 4는 2와 3의 방법 개수를 재활용해서 dp[n] = dp[n-2] + dp[n-1] 을 도출할 수 있다.
        // 단 n이 1,2,3일 때의 값을 먼저 셋팅한다.

        if (n <= 3)
            return n;

        int[] dp = new int[n];
        dp[0] = 1;
        dp[1] = 2;
        dp[2] = 3;

        for (int i = 3; i < n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }

        return dp[n - 1];
    }
}

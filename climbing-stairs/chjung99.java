class Solution {
    public int climbStairs(int n) {
        int[] dp = new int[46];
        dp[0] = 1;
        dp[1] = 1;
        dp[2] = dp[1] + dp[0];
        dp[3] = dp[2] + dp[1];

        for (int i = 4; i <= n; i++) {
            dp[i] = dp[i-1] + dp[i-2];
        }
        return dp[n];
    }
}


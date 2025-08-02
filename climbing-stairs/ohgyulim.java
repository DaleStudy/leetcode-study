class Solution {
    /* 시간 복잡도: O(N)
    * - for 루프: O(N)
    * 공간 복잡도: O(N), dp배열
    */ 
    public int climbStairs(int n) {
        if (n == 1) return 1;
        int[] dp = new int[n + 1];
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }

        return dp[n];
    }
}

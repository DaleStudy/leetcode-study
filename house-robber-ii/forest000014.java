/*
# Time Complexity: O(n)
# Space Complexity: O(n)
*/
class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        if (n == 1) return nums[0];

        int[][][] dp = new int[n][2][2];

        dp[0][0][0] = 0;
        dp[0][0][1] = 0;
        dp[0][1][0] = 0; //
        dp[0][1][1] = nums[0];
        for (int i = 1; i < n - 1; i++) {
            dp[i][0][0] = Math.max(dp[i - 1][0][0], dp[i - 1][1][0]);
            dp[i][0][1] = Math.max(dp[i - 1][0][1], dp[i - 1][1][1]);
            dp[i][1][0] = dp[i - 1][0][0] + nums[i];
            dp[i][1][1] = dp[i - 1][0][1] + nums[i];
        }

        dp[n - 1][0][0] = Math.max(dp[n - 2][0][0], dp[n - 2][1][0]);
        dp[n - 1][0][1] = Math.max(dp[n - 2][0][1], dp[n - 2][1][1]);
        dp[n - 1][1][0] = dp[n - 2][0][0] + nums[n - 1];
        dp[n - 1][1][1] = -1;

        return Math.max(Math.max(dp[n - 1][0][0], dp[n - 1][0][1]), dp[n - 1][1][0]);
    }
}

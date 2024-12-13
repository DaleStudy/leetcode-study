/*
Runtime: 0 ms(Beats: 100.00 %)
Time Complexity: O(nlogn)
- nums iteration : O(n)

Memory: 41.40 MB(Beats: 43.05 %)
Space Complexity: O(n)
- dp[n][2] : O(n) * 2 = O(n)
*/

class Solution {
    public int rob(int[] nums) {
        int[][] dp = new int[nums.length][2];

        dp[0][1] = nums[0];
        for (int i = 1; i < nums.length; i++) {
            dp[i][0] = Math.max(dp[i - 1][0], dp[i - 1][1]);
            dp[i][1] = dp[i - 1][0] + nums[i];
        }

        return Math.max(dp[nums.length - 1][0], dp[nums.length - 1][1]);
    }
}

//dp[0] -> 1번째 집 털이 수완으로 초기화
//dp[1] -> -2집 털이+지금집 털이가 -1집 털이보다 수완이 좋다. = -2집 털이(0)+지금집 털이 = 7
//dp[2] -> -2집 털이+지금집 털이가 -1집 털이보다 수완이 좋다. = -2집 털이+지금집 털이 = 11
//dp[3] -> -2집 털이+지금집 털이가 -1집 털이보다 수완이 좋다. = -2집 털이+지금집 털이 = 11 (>10)
//dp[4] -> -2집 털이+지금집 털이가 -1집 털이보다 수완이 좋다. = -2집 털이+지금집 털이 = 12 (>10)
class Solution {
    public int rob(int[] nums) {
        int[] dp = new int[nums.length];
        dp[0] = nums[0];

        for (int i = 1; i < nums.length; i++) {
            int prev2AndNowRob = (i - 2 < 0 ? 0 : dp[i - 2]) + nums[i];
            int prev1Rob = dp[i - 1];

            dp[i] = Math.max(prev2AndNowRob, prev1Rob);
        }
        return dp[nums.length - 1];
    }
}

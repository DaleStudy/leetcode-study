class Solution {
    public int maxSubArray(int[] nums) {

        int[] dp = new int[nums.length];
        dp[0] = nums[0];
        for (int i = 1; i < nums.length; i++) {
            dp[i] = Math.max(dp[i-1]+nums[i], nums[i]);
        }

        int maxVal = -987654321;
        for (int num : dp) {
            if (num > maxVal) {
                maxVal = num;
            }
        }
        return maxVal;
    }
}

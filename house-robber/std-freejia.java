class Solution {
    public int rob(int[] nums) {
        int numsLen = nums.length;
        int[] dp = new int[numsLen];

        if (numsLen == 1) return nums[0];
        dp[0] = nums[0]; 
        dp[1] = Math.max(nums[0], nums[1]); 

        for (int i = 2; i < numsLen; i++){
            dp[i] = Math.max(dp[i-2] + nums[i], dp[i-1]);
        }
        return dp[numsLen-1];
    }
}

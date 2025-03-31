/*
* solution : dp
* tc : O(n)
* sc : O(n)
*
* let dp[i] farthest point available to reach
*
* */
class Solution {
  public boolean canJump(int[] nums) {
    int[] dp = new int[nums.length];
    dp[0] = nums[0];
    for(int i = 1; i < nums.length; i++) {
      if(dp[i-1] >= i) {
        dp[i] = Math.max(nums[i] + i, dp[i-1]);
      }
    }
    return dp[dp.length-1] >= dp.length-1;
  }
}

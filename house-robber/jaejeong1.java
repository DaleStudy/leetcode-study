class Solution {
  public int rob(int[] nums) {
    // 인접한 경우는 제외한 최대 합
    // 풀이: dp로 풀이한다. dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    // TC: O(N), SC: O(N)
    if (nums.length == 1) {
      return nums[0];
    }

    var dp = new int[nums.length];
    dp[0] = nums[0];
    dp[1] = Math.max(nums[0], nums[1]);

    for (int i=2; i<nums.length; i++) {
      dp[i] = Math.max(dp[i-1], dp[i-2] + nums[i]);
    }

    return dp[nums.length-1];
  }
}

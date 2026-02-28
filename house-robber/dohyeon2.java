class Solution {
    public int rob(int[] nums) {
        // Dynamic Planning
        // Time Complexity: O(n)
        // Space Complexity: O(n) for the dp array
        // When applying DP, it is important to define the accumulated state clearly.

        if (nums.length == 1) {
            return nums[0];
        }

        // The state of dp is maximum amount of robbery at i
        int[] dp = new int[nums.length];

        dp[0] = nums[0];
        dp[1] = Math.max(nums[0], nums[1]);

        for (int i = 2; i < nums.length; i++) {
            dp[i] = Math.max(
                    // If we skip the current house,
                    // we can take the maximum amount of robbery at i - 1
                    dp[i - 1],
                    // If we rob the current house, we cannot rob the previous house
                    // so we can take the maximum amount of robbery at i - 2
                    dp[i - 2] + nums[i]);
        }

        return dp[nums.length - 1];
    }
}
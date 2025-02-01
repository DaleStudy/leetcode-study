class Solution {
    /**
    1. understanding
    - dp[n] : length of longest increasing subsequence in 0...n
    2. space
    - time: O(N^2)
    - space: O(N)
     */
    public int lengthOfLIS(int[] nums) {
        int[] dp = new int[nums.length];
        Arrays.fill(dp, 1);
        for (int i = 0; i < nums.length; i++) { // O(N)
            for (int j = 0; j <= i; j++) { // O(N)
                if (nums[j] < nums[i]) {
                    dp[i] = Math.max(dp[j]+1, dp[i]);
                }
            }
        }
        return Arrays.stream(dp).max().orElse(1);
    }
}


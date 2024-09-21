public class Solution {
    public int LengthOfLIS(int[] nums) {
        if (nums.Length == 0) return 0;

        int[] dp = new int[nums.Length];
        for (int i = 0; i < nums.Length; i++) {
            dp[i] = 1;
        }

        int maxLength = 1;
        for (int i = 1; i < nums.Length; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) {
                    dp[i] = Math.Max(dp[i], dp[j] + 1);
                }
            }
            maxLength = Math.max(maxLength, dp[i]);
        }
        
        return maxLength;
    }
}

import java.util.*;
class Solution {
    /**
     * time-complexity : O(n^2)
     * space-complexity : O(n)
     */
    public int lengthOfLIS(int[] nums) {

        int[] dp = new int[nums.length];
        Arrays.fill(dp, 1);

        for (int i = 1 ; i < nums.length; i++) {
            for (int j = i; j >= 0; j--) {
                if (nums[j] < nums[i]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
        }

        int maxVal = 0;
        for (int num : dp) {
            if (num > maxVal) maxVal = num;
        }

        return maxVal;
    }
}

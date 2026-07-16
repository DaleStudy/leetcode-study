import java.util.*;

// TC: O(n)
// SC: O(n)
class Solution {
    public int maxSubArray(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n];

        dp[n - 1] = nums[n - 1];
        int answer = dp[n - 1];

        for (int i = n - 2; i >= 0; i--) {
            dp[i] = Math.max(dp[i + 1] + nums[i], nums[i]);
            answer = Math.max(answer, dp[i]);
        }

        return answer;
    }
}

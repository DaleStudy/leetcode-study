import java.util.*;

// TC: O(n)
// SC: O(n)
class Solution {
    public int rob(int[] nums) {
        int answer = 0;

        // index 번째 집까지 털었을 때 최대
        int[] dp = new int[nums.length];
        if (nums.length == 1) return nums[0];
        if (nums.length == 2) return Math.max(nums[0], nums[1]);

        dp[0] = nums[0];
        dp[1] = Math.max(nums[0], nums[1]);

        for (int i = 2; i < nums.length; i++) {
            dp[i] = Math.max(dp[i - 1], dp[i - 2] + nums[i]);
            answer = Math.max(answer, dp[i]);
        }

        return answer;
    }
}

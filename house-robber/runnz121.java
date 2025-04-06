import java.util.Arrays;

public class runnz121 {

    public class Solution {
        public int rob(int[] nums) {

            if (nums.length == 1) {
                return nums[0];
            }

            int[] dp = new int[nums.length];

            dp[0] = nums[0];
            dp[1] = Math.max(nums[1], nums[0]);
            for (int i = 2; i < nums.length; i++) {
                int comp1 = Math.max(nums[i] + dp[i - 2], dp[i] + nums[i - 2]);
                dp[i] = Math.max(comp1, dp[i - 1]);
            }

            return Arrays.stream(dp).max().stream().findFirst().orElse(Math.max(dp[0], dp[1]));
        }
    }
}

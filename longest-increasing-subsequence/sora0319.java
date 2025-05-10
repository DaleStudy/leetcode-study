import java.util.Arrays;

class SolutionLIS {
    public int lengthOfLIS(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n];
        Arrays.fill(dp, 1);

        for (int current = 1; current < n; current++) {
            for (int prev = 0; prev < current; prev++) {
                if (nums[prev] < nums[current]) {
                    dp[current] = Math.max(dp[current], dp[prev] + 1);
                }
            }
        }

        int maxLength = 0;
        for (int len : dp) {
            maxLength = Math.max(maxLength, len);
        }
        return maxLength;
    }
}


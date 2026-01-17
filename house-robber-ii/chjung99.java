class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        if (n==1) {
            return nums[0];
        }
        return Math.max(
                robLinear(Arrays.copyOfRange(nums, 1, n)),
                robLinear(Arrays.copyOfRange(nums, 0, n-1))
        );
    }

    public int robLinear(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n];

        dp[0] = nums[0];
        if (n > 1) {
            dp[1] = Math.max(nums[0], nums[1]);
        }

        for (int i = 2; i < n; i++) {
            dp[i] = Math.max(dp[i-2] + nums[i], dp[i-1]);
        }

        return dp[n-1];
    }
}



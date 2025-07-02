class Solution {

    // DP
    public int rob(int[] nums) {
        int n = nums.length;

        if (n == 0) {
            return 0;
        }

        if (n == 1) {
            return nums[0];
        }

        int notRobbingLast = robHouses(nums, 0, n - 2);
        int notRobbingFirst = robHouses(nums, 1, n - 1);

        return Math.max(notRobbingLast, notRobbingFirst);
    }

    private int robHouses(int[] nums, int start, int end) {

        int length = end - start + 1;

        if (length == 0) {
            return 0;
        }

        if (length == 1) {
            return nums[start];
        }

        int[] dp = new int[length];

        dp[0] = nums[start];
        dp[1] = Math.max(nums[start], nums[start + 1]);

        for (int i = 2; i < length; i++) {
            dp[i] = Math.max(dp[i - 2] + nums[start + i], dp[i - 1]);
        }

        return dp[length - 1];
    }
}


class Solution {
    public int rob(int[] nums) {
        // (1) dp
        // int n = nums.length;

        // if (n == 1) return nums[0];

        // int[] dp = new int[n];

        // dp[0] = nums[0];
        // dp[1] = Math.max(nums[0], nums[1]);

        // for (int i = 2; i < n; i++) {
        //     dp[i] = Math.max(dp[i - 1], nums[i] + dp[i - 2]);
        // }

        // return dp[n - 1];

        // (2) 인접 값 비교
        int prev = 0, curr = 0;
        for (int num : nums) {
            int temp = curr;
            curr = Math.max(num + prev, curr);
            prev = temp;
        }

        return curr;
    }
}

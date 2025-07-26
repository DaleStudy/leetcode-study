class Solution {
    /* 시간 복잡도: O(N)
    * - for 루프: O(N)
    * 공간 복잡도: O(N), dp배열
    */ 
    public int rob(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n];
        dp[0] = nums[0];
        if (n > 1) dp[1] = Math.max(nums[0], nums[1]);
        for (int i = 2; i < n; i++) {
            dp[i] = Math.max(dp[i - 2] + nums[i], dp[i - 1]);
        }

        return dp[n - 1];
    }
}


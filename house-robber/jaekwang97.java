class Solution {
    public int rob(int[] nums) {
        int answer = 0;

        int n = nums.length;
        int[][] dp = new int[n + 1][2];

        // 0 -> 현재 인덱스 선택 o
        // 1 -> 현재 인덱스 선택 x
        for (int i = 1; i <= n; i++) {
            dp[i][0] = dp[i - 1][1] + nums[i - 1];
            dp[i][1] = Math.max(dp[i - 1][0], dp[i - 1][1]);
        }

        answer = Math.max(dp[n][0], dp[n][1]);

        return answer;
    }
}

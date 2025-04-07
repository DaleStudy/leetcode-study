// 시간 복잡도: O(n) - dp 배열을 한 번 순회
// 공간 복잡도: O(n) - dp 배열
class Solution {
    public int rob(int[] nums) {
       int[][] dp = new int[nums.length][2]; // 0: not robbed, 1: robbed

        if(nums.length == 0) return 0;
        if(nums.length == 1) return nums[0];

        dp[0][0] = 0;
        dp[0][1] = nums[0];

        for(int i = 1; i < nums.length; i++){
            dp[i][0] = Math.max(dp[i-1][0], dp[i-1][1]);
            dp[i][1] = dp[i-1][0] + nums[i];
        }

        return Math.max(dp[nums.length-1][0], dp[nums.length-1][1]);
    }
}


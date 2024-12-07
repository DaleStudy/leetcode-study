class Solution {
    public int rob(int[] nums) {
        //배열 길이 0이면 털 수 있는 집이 없음.
        if (nums.length == 0) return 0;
        //배열 길이가 1이면 한 집만 털 수 있음.
        if (nums.length == 1) return nums[0];

        //동적 계획법으로 풀이
        int[] dp = new int[nums.length];
        dp[0] = nums[0];
        dp[1] = Math.max(nums[0], nums[1]);

        //배열 크기가 2이상일 경우 최대 금액의 범위 확장
        for (int i = 2; i < nums.length; i++) {
            dp[i] = Math.max(dp[i - 2] + nums[i], dp[i - 1]);
        }
        return dp[nums.length - 1];
    }
}

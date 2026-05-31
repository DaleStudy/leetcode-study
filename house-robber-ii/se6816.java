class Solution {
    public int rob(int[] nums) {
        if(nums.length == 1) {
            return nums[0];
        }

        // 첫 집을 턴 경우
        int[] dp = new int[nums.length];
        dp[0] = nums[0];
        if(nums.length != 1) {
            dp[1] = Math.max(nums[0], nums[1]);
        }

        for (int i = 2; i < nums.length; i++) {
            dp[i] = Math.max(dp[i-1], nums[i] + dp[i-2]);
        }

        // 첫 집 안 턴 경우 
        int[] dp2 = new int[nums.length-1];
        dp2[0] = nums[1];      
        if (nums.length > 2) {
            dp2[1] = Math.max(nums[1], nums[2]);
        }
        for (int i = 2; i < nums.length-1; i++) {
            dp2[i] = Math.max(dp2[i-1], nums[i+1] + dp2[i-2]);  
        }

        return Math.max(dp[nums.length-2], dp2[nums.length-2]);
    }
}

class Solution {
    /* 시간 복잡도: O(N)
    * - for 루프: O(N)
    * 공간 복잡도: O(N), dp배열
    */ 
    public int maxSubArray(int[] nums) {
        int[] dp = new int[nums.length];
        dp[0] = nums[0];
        
        int answer = nums[0];
        for (int i = 1; i < nums.length; i++) {
            dp[i] = Math.max(nums[i], dp[i - 1] + nums[i]);
            answer = Math.max(answer, dp[i]);
        }
        return answer;
    }
}

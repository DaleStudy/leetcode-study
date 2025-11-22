/**
Problem 198 : House Robber
Summary : 
- dp를 이용하여, 이전 결과를 저장하면서 문제를 해결한다.

*/

class Solution {
    public int rob(int[] nums) {
        int[] dp = new int[nums.length+1];
        dp[1] = nums[0];
        if(nums.length != 1) {
            dp[2] = nums[1];
        }

        for(int i = 2; i < nums.length; i++) {
            dp[i+1] = Math.max((nums[i] + dp[i-1]), (nums[i] + dp[i-2]));
        }

        return Math.max(dp[nums.length], dp[nums.length-1]);
    }
}

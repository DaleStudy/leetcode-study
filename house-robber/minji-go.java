/*
    Problem: https://leetcode.com/problems/house-robber/
    Description: the maximum amount of money you can rob if you cannot rob two adjacent houses
    Concept: Array, Dynamic Programming
    Time Complexity: O(n), Runtime: 0ms
    Space Complexity: O(1), Memory: 41.42MB
*/
class Solution {
    public int rob(int[] nums) {
        int sum1 = nums[0];
        int sum2 = nums.length>1? Math.max(nums[0], nums[1]) : nums[0];
        for(int i=2; i<nums.length; i++){
            int sum3=Math.max(nums[i]+sum1,sum2);
            sum1=sum2;
            sum2=sum3;
        }
        return sum2;
    }
}

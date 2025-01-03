/*
    Problem: https://leetcode.com/problems/maximum-subarray/
    Description: return the largest sum of the subarray, contiguous non-empty sequence of elements within an array.
    Concept: Array, Divide and Conquer, Dynamic Programming
    Time Complexity: O(N), Runtime 1ms
    Space Complexity: O(1), Memory 57.02MB
*/
class Solution {
    public int maxSubArray(int[] nums) {
        int max = nums[0];
        int sum = nums[0];
        for(int i=1; i<nums.length; i++){
            sum = Math.max(nums[i], nums[i]+sum);
            max = Math.max(max, sum);
        }
        return max;
    }
}

/**
 * https://leetcode.com/problems/missing-number/
 *
 * time: O(n)
 * space: O(1)
 */
class Solution {
    public int missingNumber(int[] nums) {
        int sum = nums.length * (nums.length+1) / 2;
        for (int num : nums) {
            sum -= num;
        }
        return sum;
    }
}

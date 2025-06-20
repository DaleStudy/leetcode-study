/**
 * <a href="https://leetcode.com/problems/missing-number/">week11-1. missing-number</a>
 * <li>Description: Return the only number in the range that is missing from the array</li>
 * <li>Topics: Array, Hash Table, Math, Binary Search, Bit Manipulation, Sorting </li>
 * <li>Time Complexity: O(N), Runtime 0ms       </li>
 * <li>Space Complexity: O(1), Memory 45.67MB   </li>
 */
class Solution {
    public int missingNumber(int[] nums) {
        int sum = (nums.length) * (nums.length + 1) / 2;
        for (int i = 0; i < nums.length; i++) {
            sum -= nums[i];
        }
        return sum;
    }
}

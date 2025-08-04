/**
 * <a href="https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/">find-minimum-in-rotated-sorted-array</a>
 * <li>Description: Given the sorted rotated array nums of unique elements, return the minimum element of this array</li>
 * <li>Topics: Array, Binary Search</li>
 * <li>Time Complexity: O(logN), Runtime 0ms</li>
 * <li>Space Complexity: O(1), Memory 41.78MB</li>
 */

class Solution {
    public int findMin(int[] nums) {
        if (nums[0] <= nums[nums.length - 1]) {
            return nums[0];
        }

        int left = 0, right = nums.length - 1;
        while (left < right) {
            int mid = (left + right + 1) / 2;
            if (nums[left] < nums[mid]) {
                left = mid;
            } else {
                right = mid - 1;
            }
        }

        return nums[left + 1];
    }
}

/**
 * https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
 *
 * time: O(log N)
 * space: O(1)
 */
class Solution {

    public int findMin(int[] nums) {
        int left = 0;
        int right = nums.length - 1;
        while (nums[left] > nums[right]) {
            int mid = (left + right) / 2;
            if (nums[mid] < nums[right]) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return nums[left];
    }
}

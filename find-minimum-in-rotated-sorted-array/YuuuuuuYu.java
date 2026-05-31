/**
 * Runtime: 0ms
 * Time Complexity: O(log n)
 *
 * Memory: 43.81MB
 * Space Complexity: O(1)
 *
 * Approach: 이진 탐색
 */
class Solution {
    public int findMin(int[] nums) {
        int left = 0;
        int right = nums.length-1;

        while (left < right) {
            int mid = left + (right-left)/2;
            if (nums[mid] <= nums[right]) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        return nums[left];
    }
}

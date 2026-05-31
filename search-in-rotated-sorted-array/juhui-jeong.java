/**
 * 시간 복잡도: O(log n)
 * 공간 복잡도: O(1)
 */
class Solution {
    public int search(int[] nums, int target) {
        int low = 0;
        int high = nums.length - 1;

        while (low <= high) {
            int mid = (low + high) / 2;
            
            if (nums[mid] == target) {
                return mid;
            }
            // 왼쪽 구간이 정렬된 경우
            if (nums[low] <= nums[mid]) {
                if (nums[low] <= target && target < nums[mid]) {
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            // 오른쪽 구간이 정렬된 경우
            } else {
                if (nums[mid] < target && target <= nums[high]) {
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }
        }
        return -1;
    }
}

class Solution {
    // 공간복잡도: O(1), 시간복잡도: O(logn)
    public int search(int[] nums, int target) {
        int left = 0, right = nums.length - 1;

        while (left < right) {
            int mid = (left + right) / 2;

            // 오른쪽 정렬
            if (nums[mid] < nums[right]) {
                if (nums[mid] <= target && target <= nums[right]) {
                    if (nums[mid] == target) return mid;
                    left = mid + 1;
                }
                else right = mid - 1;
            // 왼쪽 정렬
            } else {
                if (nums[left] <= target && target <= nums[mid]) {
                    if (nums[mid] == target) return mid;
                    right = mid - 1;
                }
                else left = mid + 1;
            }
        }

        return nums[left] == target ? left : -1;
    }
}

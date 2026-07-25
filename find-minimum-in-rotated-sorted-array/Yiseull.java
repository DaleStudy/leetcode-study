class Solution {
    public int findMin(int[] nums) {
        return binarySearch(nums);
    }

    // 공간복잡도: O(1), 시간복잡도: O(logn)
    private int binarySearch(int[] nums) {
        int left = 0, right = nums.length - 1;

        while (left < right) {
            if (nums[left] <= nums[right]) return nums[left];

            int mid = (left + right) / 2;

            if (nums[right] < nums[mid]) left = mid + 1;
            else right = mid;
        }

        return nums[left];
    }
}

public class Solution {
    public int search(int[] nums, int target) {
        int p = findPivot(nums);

        int index = binarySearch(nums, 0, p - 1, target);
        if (index != -1) {
            return index;
        }
        return binarySearch(nums, p, nums.length - 1, target);
    }

    private int findPivot(int[] nums) {
        int l = 0;
        int h = nums.length - 1;

        while (l <= h) {
            int mid = l + (h - l) / 2;

            if (mid > 0 && nums[mid - 1] > nums[mid]) {
                return mid;
            }

            if (nums[0] <= nums[mid]) {
                l = mid + 1;
            } else {
                h = mid - 1;
            }
        }

        return 0;
    }

    private int binarySearch(int[] nums, int l, int h, int target) {
        while (l <= h) {
            int mid = l + (h - l) / 2;

            if (nums[mid] == target) {
                return mid;
            }

            if (nums[mid] < target) {
                l = mid + 1;
            } else {
                h = mid - 1;
            }
        }

        return -1;
    }
}


import java.util.*;

// TC: O(log n)
// SC: O(1)
class Solution {
    public int search(int[] nums, int target) {
        int pivot = findRotationPoint(nums);

        if (pivot > 0 && target >= nums[0]) {
            return binarySearch(nums, target, 0, pivot - 1);
        }
        return binarySearch(nums, target, pivot, nums.length - 1);
    }

    private int findRotationPoint(int[] nums) {
        int lo = 0;
        int hi = nums.length - 1;

        while (lo < hi) {
            if (nums[lo] < nums[hi]) {
                return lo;
            }

            int mid = (lo + hi) / 2;
            if (nums[lo] <= nums[mid]) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }

        return lo;
    }

    private int binarySearch(int[] nums, int target, int lo, int hi) {
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (nums[mid] == target) {
                return mid;
            }
            if (nums[mid] < target) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }

        return -1;
    }
}

/*
# Time Complexity : O(nlogn)
# Space Complexity : O(1)
*/

class Solution {
    public int search(int[] nums, int target) {
        if (nums[0] == target) return 0;
        boolean prev;
        if (nums[0] < target) prev = true;
        else prev = false;

        int l, r, m, pivot = nums.length - 1;
        l = 0;
        r = nums.length - 1;
        while (l <= r) {
            m = (r - l) / 2 + l;
            if (m == nums.length - 1 || nums[m] > nums[m + 1]) {
                pivot = m;
                break;
            } else if (nums[0] <= nums[m]) {
                l = m + 1;
            } else {
                r = m - 1;
            }
        }

        if (prev) {
            l = 0;
            r = pivot;
        } else {
            l = pivot + 1;
            r = nums.length - 1;
        }

        while (l <= r) {
            m = (r - l) / 2 + l;
            if (nums[m] == target) return m;
            else if (nums[m] < target) l = m + 1;
            else r = m - 1;
        }
        return -1;
    }
}

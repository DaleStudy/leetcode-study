class Solution {
    /*
    time complexity: O(log n)
    space complexity: O(h)
     */
    public int findMin(int[] nums) {
        int start = 0, end = nums.length - 1;

        if (nums[start] < nums[end]) return nums[start];

        while (start < end) {
            int mid = start + (end - start) / 2;

            if (nums[mid] < nums[end]) {
                end = mid;
            } else {
                start = mid + 1;
            }
        }
        return nums[start];
    }
}

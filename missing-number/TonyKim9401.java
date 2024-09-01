// TC: O(n log n)
// SC: O(n)
class Solution {
    public int missingNumber(int[] nums) {
        Arrays.sort(nums);
        int idx = 1;
        int n = nums.length;
        for (; idx < n; idx++) {
            if (nums[idx] - 1 != nums[idx-1]) return nums[idx] - 1;
        }
        return nums[idx-1] == n ? 0 : n;
    }
}

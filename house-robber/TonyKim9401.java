// TC: O(n)
// always need to check every case
// SC: O(n)
// the length of the result int list is same with the length of the given nums int list
class Solution {
    public int rob(int[] nums) {
        int[] result = new int[nums.length];

        if (nums.length < 2) return nums[0];
        if (nums.length < 3) return Math.max(nums[0], nums[1]);

        result[0] = nums[0];
        result[1] = Math.max(nums[0], nums[1]);

        for (int i = 2; i < nums.length; i++) {
            result[i] = Math.max(result[i - 1], result[i - 2] + nums[i]);
        }

        return result[nums.length-1];
    }
}

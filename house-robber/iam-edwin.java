class Solution {
    public int rob(int[] nums) {
        int[] result = new int[nums.length + 2];

        for (int index = nums.length - 1; index >= 0; index--) {
            int robFirst = nums[index] + result[index + 2];
            int passFirst = result[index + 1];
            result[index] = Integer.max(robFirst, passFirst);
        }

        return result[0];
    }
}

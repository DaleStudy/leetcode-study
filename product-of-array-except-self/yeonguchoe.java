class Solution {
    // Time complexity: O(n)
    // Space complexity: O(n)
    public int[] productExceptSelf(int[] nums) {
        int[] leftMultiplier = new int[nums.length];
        int[] rightMultiplier = new int[nums.length];

        leftMultiplier[0] = 1;
        for (int i = 0; i < nums.length - 1; i++) {
            leftMultiplier[i + 1] = nums[i] * leftMultiplier[i];
        }

        rightMultiplier[nums.length - 1] = 1;
        for (int i = nums.length - 1; i > 0; i--) {
            rightMultiplier[i - 1] = nums[i] * rightMultiplier[i];
        }

        int[] result = new int[nums.length];
        for (int i = 0; i < result.length; i++) {
            result[i] = leftMultiplier[i] * rightMultiplier[i];
        }
        return result;
    }
}

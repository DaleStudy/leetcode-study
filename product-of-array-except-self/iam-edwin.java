class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] left = new int[nums.length + 1];
        int[] right = new int[nums.length + 1];
        left[0] = 1;
        right[nums.length] = 1;

        for (int i = 0; i < nums.length; i++) {
            left[i + 1] = left[i] * nums[i];
            right[nums.length - i - 1] = right[nums.length - i] * nums[nums.length - i - 1];
        }

        int[] result = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            result[i] = left[i] * right[i + 1];
        }
        return result;
    }
}

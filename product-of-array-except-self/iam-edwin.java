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

    public int[] productExceptSelfV2(int[] nums) {
        int[] result = new int[nums.length];

        int curr = 1;
        result[0] = curr;
        for (int i = 1; i < nums.length; i++) {
            curr *= nums[i - 1];
            result[i] = curr;
        }

        curr = 1;
        result[nums.length - 1] *= curr;
        for (int i = nums.length - 2; i >= 0; i--) {
            curr *= nums[i + 1];
            result[i] *= curr;
        }

        return result;
    }
}

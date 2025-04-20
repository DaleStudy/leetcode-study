class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] res = new int[nums.length];

        res[0] = 1;
        for (int i = 1; i < nums.length; i++) {
            res[i] = res[i - 1] * nums[i - 1];
        }

        int acc = 1;
        for (int i = nums.length - 2; i >= 0; i--) {
            acc *= nums[i + 1];
            res[i] *= acc;
        }

        return res;
    }
}

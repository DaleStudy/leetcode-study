class Solution {
    public int[] productExceptSelf(int[] nums) {
        // time complexity: O(n)
        // space complexity: O(n)
        int[] left = new int[nums.length];
        int[] right = new int[nums.length];

        // nums =  [1,  2,  3, 4]

        // left =  [1,  1,  2, 6]
        // right = [24, 12, 4, 1]

        // nums => [24, 12, 8, 6]
        left[0] = 1;
        for (int i = 1; i < nums.length; i++) {
            left[i] = left[i-1] * nums[i-1];
        }

        right[right.length-1] = 1;
        for (int i = nums.length - 2; i >= 0; i--) {
            right[i] = right[i+1] * nums[i+1];
        }

        for (int i = 0; i < nums.length; i++) {
            nums[i] = left[i] * right[i];
        }
        return nums;
    }
}

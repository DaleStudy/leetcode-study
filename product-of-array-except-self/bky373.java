/**
 * time: O(N)
 * space: O(N)
 */
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int len = nums.length;
        int[] res = new int[len];
        int[] left = Arrays.copyOf(nums, len);
        int[] right = Arrays.copyOf(nums, len);
        for (int i = 1; i < len; i++) {
            left[i] *= left[i - 1];
        }
        for (int i = len - 2; i >= 0; i--) {
            right[i] *= right[i + 1];
        }
        for (int i = 1; i < len - 1; i++) {
            res[i] = left[i - 1] * right[i + 1];
        }
        res[0] = right[1];
        res[len - 1] = left[len - 2];
        return res;
    }
}

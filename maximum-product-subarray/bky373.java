// time: O(N)
// space: O(1)
class Solution {

    public int maxProduct(int[] nums) {
        double max = Integer.MIN_VALUE;
        double product = 1;

        for (int num : nums) {
            product *= num;
            max = Math.max(product, max);
            if (product == 0) {
                product = 1;
            }

        }

        product = 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            product *= nums[i];
            max = Math.max(product, max);
            if (product == 0) {
                product = 1;
            }
        }

        return (int) max;
    }
}

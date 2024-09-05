// TC: O(n)
// SC: O(1)
class Solution {
    public int maxProduct(int[] nums) {
        int currentMax = nums[0];
        int currentMin = nums[0];
        int maxProduct = nums[0];

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] < 0) {
                int temp = currentMax;
                currentMax = currentMin;
                currentMin = temp;
            }

            currentMax = Math.max(nums[i], currentMax * nums[i]);
            currentMin = Math.min(nums[i], currentMin * nums[i]);

            maxProduct = Math.max(maxProduct, currentMax);
        }

        return maxProduct;
    }
}

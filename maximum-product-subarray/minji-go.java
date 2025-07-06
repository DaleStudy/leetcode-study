/**
 * <a href="https://leetcode.com/problems/maximum-product-subarray/">week9-3. maximum-product-subarray</a>
 * <li>Description: Given an integer array nums, find a subarray that has the largest product, and return the product. </li>
 * <li>Topics: Array, Dynamic Programming       </li>
 * <li>Time Complexity: O(N), Runtime 2ms       </li>
 * <li>Space Complexity: O(1), Memory 45.42MB   </li>
 */
class Solution {
    public int maxProduct(int[] nums) {
        int maxSoFar = nums[0];
        int minSoFar = nums[0];
        int result = nums[0];

        for (int i = 1; i < nums.length; i++) {
            int cur = nums[i];
            int tempMax = maxSoFar;

            maxSoFar = Math.max(cur, Math.max(cur * maxSoFar, cur * minSoFar));
            minSoFar = Math.min(cur, Math.min(cur * tempMax, cur * minSoFar));

            result = Math.max(result, maxSoFar);
        }

        return result;
    }
}

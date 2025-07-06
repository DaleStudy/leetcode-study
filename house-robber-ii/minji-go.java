/**
 * <a href="https://leetcode.com/problems/house-robber-ii/">week14-3. house-robber-ii</a>
 * <li>Description: Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police</li>
 * <li>Topics: Array, Dynamic Programming   </li>
 * <li>Time Complexity: O(N), Runtime 0ms   </li>
 * <li>Space Complexity: O(1), Memory 40.6MB</li>
 */

class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        if (n == 1) return nums[0];
        if (n == 2) return Math.max(nums[0], nums[1]);

        return Math.max(rob(nums, 0, n - 2), rob(nums, 1, n - 1));
    }

    public int rob(int[] nums, int start, int end) {
        int prev1 = 0, prev2 = 0;
        for (int i = start; i <= end; i++) {
            int temp = Math.max(prev2, prev1 + nums[i]);
            prev1 = prev2;
            prev2 = temp;
        }
        return prev2;
    }
}

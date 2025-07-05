// https://leetcode.com/problems/house-robber-ii/description/
class Solution {
    fun rob(nums: IntArray): Int {
        if (nums.size == 1) return nums[0]
        return maxOf(rob(nums, 0, nums.size - 2), rob(nums, 1, nums.size - 1))
    }

    private fun rob(nums: IntArray, start: Int, end: Int): Int {
        val dp = IntArray(nums.size) { 0 }
        dp[start] = nums[start]
        dp[start + 1] = maxOf(nums[start], nums[start + 1])
        for (i in start + 2..end) {
            dp[i] = maxOf(dp[i - 1], dp[i - 2] + nums[i])
        }
        return dp[end]
    }
}
// TC: O(n)
// SC: O(n)

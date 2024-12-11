package leetcode_study

import java.lang.Integer.max

class Solution {
    fun rob(nums: IntArray): Int {
        return max(rob_recursion(nums, 0), rob_recursion(nums, 1))
    }

    private fun rob_recursion(nums: IntArray, index: Int): Int {
        if (index >= nums.size) {
            return 0
        }
        return nums[index] + rob_recursion(nums, index + 2)
    }
}

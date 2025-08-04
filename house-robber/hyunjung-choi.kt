package leetcode_study

class Solution {
    fun rob(nums: IntArray): Int {
        if (nums.size == 1) return nums[0]

        var prev2 = nums[0]
        var prev1 = maxOf(nums[0], nums[1])

        for (i in 2 until nums.size) {
            val current = maxOf(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = current
        }

        return prev1
    }
}

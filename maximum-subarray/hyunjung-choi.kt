class Solution {
    fun maxSubArray(nums: IntArray): Int {
        var currentSum = nums[0]
        var maxSum = nums[0]

        for (i in 1 until nums.size) {
            currentSum = if (currentSum < 0) nums[i] else currentSum + nums[i]
            maxSum = maxOf(currentSum, maxSum)
        }

        return maxSum
    }
}

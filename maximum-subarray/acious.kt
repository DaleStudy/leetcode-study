class Solution {
    fun maxSubArray(nums: IntArray): Int {
        var maxSum = nums[0]
        var sum = 0

        for(num in nums) {
            sum = max(sum+num, num)
            maxSum = max(sum, maxSum)
        }

        return maxSum
    }
}
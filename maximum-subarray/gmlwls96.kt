class Solution {
    fun maxSubArray(nums: IntArray): Int {
        val dp = Array(nums.size) { y ->
            IntArray(nums.size) { x ->
                if (y == x) {
                    nums[y]
                } else {
                    0
                }
            }
        }

        var max = dp[0][0]
        for (y in nums.indices) {
            for (x in y + 1..nums.lastIndex) {
                dp[y][x] = dp[y][x - 1] + nums[x]
                max = max(max, dp[y][x])
            }
        }
        return max
    }
}

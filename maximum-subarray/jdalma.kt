package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test
import kotlin.math.max

class `maximum-subarray` {

    fun maxSubArray(nums: IntArray): Int {
        return usingDP(nums)
    }

    /**
     * TC: O(n), SC: O(n)
     */
    private fun usingDP(nums: IntArray): Int {
        val dp = IntArray(nums.size).apply {
            this[0] = nums[0]
        }

        for (index in 1 until nums.size) {
            dp[index] = max(nums[index], nums[index] + dp[index - 1])
        }

        return dp.max()
    }

    /**
     * TC: O(n), SC: O(1)
     */
    private fun usingKadane(nums: IntArray): Int {
        var (current, max) = nums[0] to nums[0]

        for (index in 1 until nums.size) {
            current = max(nums[index], current + nums[index])
            max = max(max, current)
        }

        return max
    }

    @Test
    fun `정수 배열의 하위 배열 중 가장 큰 합을 반환한다`() {
        maxSubArray(intArrayOf(-2,1,-3,4,-1,2,1,-5,4)) shouldBe 6
        maxSubArray(intArrayOf(1)) shouldBe 1
        maxSubArray(intArrayOf(5,4,-1,7,8)) shouldBe 23
    }
}

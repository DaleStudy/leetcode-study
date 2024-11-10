package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test
import kotlin.math.max

class `house-robber` {

    fun rob(nums: IntArray): Int {
        return usingDP(nums)
    }

    /**
     * TC: O(n), SC: O(n)
     */
    private fun usingDP(nums: IntArray): Int {
        val dp = IntArray(nums.size + 1).apply {
            this[0] = 0
            this[1] = nums[0]
        }
        for (index in 1 until nums.size) {
            dp[index + 1] = max(nums[index] + dp[index - 1], dp[index])
        }

        return dp[nums.size]
    }

    /**
     * TC: O(n), SC: O(n)
     */
    private fun usingMemoization(nums: IntArray): Int {
        val memo = IntArray(nums.size) { -1 }
        fun recursive(index: Int): Int {
            return if (index > nums.size - 1) 0
            else if (memo[index] != -1) memo[index]
            else {
                memo[index] = max(nums[index] + recursive(index + 2), recursive(index + 1))
                memo[index]
            }
        }

        return recursive(0)
    }

    /**
     * 시간초과
     * TC: O(2^n), SC: O(n)
     */
    private fun usingRecursive(nums:IntArray): Int {
        fun recursive(index: Int, depth: Int): Int {
            if (index > nums.size - 1) return 0
            println("${"-".repeat(depth)} : max($index + ${index + 2}, ${index + 1})")
            return max(nums[index] + recursive(index + 2, depth + 1), recursive(index + 1, depth + 1))
        }

        return recursive(0, 0)
    }

    @Test
    fun `인접하지 않은 원소를 선택하여 최대의 합을 반환한다`() {
        rob(intArrayOf(1,2,3,1)) shouldBe 4
        rob(intArrayOf(2,7,9,3,1)) shouldBe 12
        rob(intArrayOf(8,7,9,11,1)) shouldBe 19
    }
}

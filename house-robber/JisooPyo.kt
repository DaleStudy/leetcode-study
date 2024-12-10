package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test
import kotlin.math.max

/**
 * Leetcode
 * 198. House Robber
 * Medium
 *
 * 사용된 알고리즘: Dynamic Programming
 *
 * i번째 집에서 얻을 수 있는 최대 금액은 다음 두 가지 중 큰 값입니다.
 *   - (i-2)번째 집까지의 최대 금액 + 현재 집의 금액
 *   - (i-1)번째 집까지의 최대 금액
 */
class HouseRobber {
    /**
     * Runtime: 0 ms(Beats: 100.00 %)
     * Time Complexity: O(n)
     *
     * Memory: 34.65 MB(Beats: 40.50 %)
     * Space Complexity: O(n)
     */
    fun rob(nums: IntArray): Int {
        if (nums.size == 1) {
            return nums[0]
        }
        if (nums.size == 2) {
            return max(nums[0], nums[1])
        }
        val dp = IntArray(nums.size)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for (i in 2 until nums.size) {
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        }
        return dp[nums.size - 1]
    }

    /**
     * 공간 복잡도를 개선
     * Runtime: 0 ms(Beats: 100.00 %)
     * Time Complexity: O(n)
     *
     * Memory: 34.95 MB(Beats: 36.98 %)
     * Space Complexity: O(1)
     */
    fun rob2(nums: IntArray): Int {
        if (nums.size == 1) return nums[0]
        if (nums.size == 2) return max(nums[0], nums[1])

        var twoBack = nums[0]
        var oneBack = max(nums[0], nums[1])
        var current = oneBack

        for (i in 2 until nums.size) {
            current = max(twoBack + nums[i], oneBack)
            twoBack = oneBack
            oneBack = current
        }

        return current
    }

    @Test
    fun test() {
        rob(intArrayOf(1, 2, 3, 1)) shouldBe 4
        rob(intArrayOf(2, 7, 9, 3, 1)) shouldBe 12
        rob2(intArrayOf(1, 2, 3, 1)) shouldBe 4
        rob2(intArrayOf(2, 7, 9, 3, 1)) shouldBe 12
    }
}

package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test
import kotlin.math.max

class `jump-game` {

    fun canJump(nums: IntArray): Boolean {
        return usingGreedy(nums)
    }

    /**
     * TC: O(n), SC: O(1)
     */
    private fun usingGreedy(nums: IntArray): Boolean {
        var reachable = 0
        for (index in nums.indices) {
            if (index > reachable) return false
            reachable = max(reachable, index + nums[index])
        }

        return true
    }

    /**
     * TC: O(n^2), SC: O(n)
     */
    private fun usingMemoization(nums: IntArray): Boolean {
        val memo = IntArray(nums.size) { -1 }
        fun dfs(now: Int): Boolean {
            if (now >= nums.size - 1) {
                return true
            } else if (memo[now] != -1) {
                return memo[now] != 0
            }
            for (next in 1 .. nums[now]) {
                if (dfs(now + next)) {
                    memo[now] = 1
                    return true
                }
            }
            memo[now] = 0
            return false
        }
        return dfs(0)
    }

    @Test
    fun `첫 번째 인덱스에서 마지막 인덱스에 도달할 수 있는지 여부를 반환한다`() {
        canJump(intArrayOf(2,3,1,1,4)) shouldBe true
        canJump(intArrayOf(3,2,1,0,4)) shouldBe false
    }
}

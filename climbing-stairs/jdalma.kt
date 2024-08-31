package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

class `climbing-stairs` {

    /**
     * 1. bottom-up 방식으로 가능한 경우의 수를 누적한다.
     * TC: O(n), SC: O(n)
     */
    fun climbStairs(n: Int): Int {
        val dp = IntArray(n + 1).apply {
            this[1] = 1
            if (n >= 2) this[2] = 2
        }

        for (num in 3 .. n) {
            dp[num] = dp[num - 1] + dp[num - 2]
        }

        return dp[n]
    }

    @Test
    fun `입력받은 목푯값에 1과 2만 더하여 도달할 수 있는 경우의 수를 반환한다`() {
        climbStairs(1) shouldBe 1
        climbStairs(2) shouldBe 2
        climbStairs(3) shouldBe 3
        climbStairs(4) shouldBe 5
    }
}

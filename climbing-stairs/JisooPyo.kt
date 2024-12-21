package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

/**
 * Leetcode
 * 70. Climbing Stairs
 * Easy
 *
 * 사용된 알고리즘: Dynamic Programming
 * n개의 계단을 오르는 방법 = n-1개의 계단을 오르는 방법 수 + n-2개의 계단을 오르는 방법
 */
class ClimbingStairs {
    /**
     * Runtime: 0 ms(Beats: 100.00 %)
     * Time Complexity: O(n)
     *   - 배열 순회
     *
     * Memory: 33.94 MB(Beats: 18.06 %)
     * Space Complexity: O(n)
     *   - n+1 크기의 배열 사용
     */
    fun climbStairs1(n: Int): Int {
        if (n == 1) return 1
        if (n == 2) return 2

        val arr = IntArray(n + 1)
        arr[1] = 1
        arr[2] = 2
        for (i in 3..n) {
            arr[i] = arr[i - 1] + arr[i - 2]
        }
        return arr[n]
    }

    /**
     * 배열을 쓰지 않고 변수를 사용하여 공간 복잡도를 개선한 버전입니다.
     * Runtime: 0 ms(Beats: 100.00 %)
     * Time Complexity: O(n)
     *   - n번 순회
     *
     * Memory: 34.06 MB(Beats: 15.90 %)
     * Space Complexity: O(1)
     *   - 사용되는 추가 공간이 입력 크기와 무관하게 일정함
     */
    fun climbStairs2(n: Int): Int {
        if (n == 1 || n == 2) return n
        var firstCase = 1
        var secondCase = 2
        var totalSteps = 0

        for (steps in 3..n) {
            totalSteps = firstCase + secondCase
            firstCase = secondCase
            secondCase = totalSteps
        }
        return totalSteps
    }

    @Test
    fun test() {
        climbStairs1(2) shouldBe 2
        climbStairs1(3) shouldBe 3
        climbStairs2(2) shouldBe 2
        climbStairs2(3) shouldBe 3
    }
}

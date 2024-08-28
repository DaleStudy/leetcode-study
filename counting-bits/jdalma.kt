package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

class `counting-bits` {

    fun countBits(n: Int): IntArray {
        return usingDPAndLeastSignificantBit(n)
    }

    // 1. 입력받은 정수만큼 순회하며 bit 카운트
    // 시간복잡도: O(n * log(n)), 공간복잡도: O(1)
    private fun usingBinary(n: Int): IntArray {
        fun binary(n: Int): Int {
            var calc = n
            var count = 0
            while(calc > 0) {
                if (calc % 2 != 0) {
                    count++
                }
                calc /= 2
            }
            return count
        }

        return (0 .. n).map { binary(it) }.toIntArray()
    }

    // 2. MSB, 즉 최상위 비트를 활용하여 십진수가 두 배가 될때마다 MSB를 갱신하여 이전의 결과를 활용
    // 시간복잡도: O(n), 공간복잡도: O(n)
    private fun usingDPAndMostSignificantBit(n: Int): IntArray {
        val dp = IntArray(n + 1)
        var msb = 1

        for (index in 1 .. n) {
           if (index == msb shl 1) {
               msb = index
           }
            dp[index] = 1 + dp[index - msb]
        }

        return dp
    }

    // 3. 최하위 비트를 제거한 결과를 재활용한다. (최하위 비트를 제거한 결과) + (현재 십진수의 최하위비트)
    // 시간복잡도: O(n), 공간복잡도: O(n)
    private fun usingDPAndLeastSignificantBit(n: Int): IntArray {
        val dp = IntArray(n + 1)
        for (index in 1 .. n) {
            dp[index] = dp[index shr 1] + (index and 1)
        }

        return dp
    }

    @Test
    fun `정수가 주어지면 각 i(0 ~ i)에 대해 이진 표현에서 1의 개수를 저장하는 배열을 반환한다`() {
        countBits(2) shouldBe intArrayOf(0,1,1)
        countBits(5) shouldBe intArrayOf(0,1,1,2,1,2)
    }
}

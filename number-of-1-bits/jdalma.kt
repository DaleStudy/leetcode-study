package leetcode_study

import io.kotest.matchers.equals.shouldBeEqual
import org.junit.jupiter.api.Test

class `number-of-1-bits` {

    fun hammingWeight(n: Int): Int {
        return bitOperation(n)
    }

    // 1. 직접 2진수를 구함
    // 시간복잡도: O(log n), 공간복잡도: O(1)
    private fun binary(n: Int): Int {
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

    // 2. 비트 논리 연산자 사용
    // 시간복잡도: O(log n), 공간복잡도: O(1)
    private fun bitOperation(n: Int): Int {
        var calc = n
        var count = 0
        while (calc > 0) {
            if (calc and 1 == 1) {
                count ++
            }
            calc = calc shr 1
        }
        return count
    }

    @Test
    fun `이진수에서_0이_아닌_성분의_개수를 반환한다`() {
        hammingWeight(11) shouldBeEqual 3
        hammingWeight(128) shouldBeEqual 1
        hammingWeight(2147483645) shouldBeEqual 30
    }
}

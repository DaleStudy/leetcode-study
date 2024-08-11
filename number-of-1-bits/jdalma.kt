package leetcode_study

import io.kotest.matchers.equals.shouldBeEqual
import org.junit.jupiter.api.Test

class `number-of-1-bits` {

    fun hammingWeight(n: Int): Int {
        return second(n)
    }

    private fun first(n: Int): Int {
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

    private fun second(n: Int): Int {
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

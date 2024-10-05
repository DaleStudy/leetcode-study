package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test
import kotlin.math.max

class `longest-repeating-character-replacement` {

    fun characterReplacement(s: String, k: Int): Int {
        return usingSlidingWindow(s, k)
    }

    /**
     * TC: O(n^3), SC: O(1) 시간초과 !!!
     */
    private fun usingBruteForce(s: String, k: Int): Int {
        var result = 0

        for (start in s.indices) {
            for (end in start until s.length) {
                val counter = mutableMapOf<Char, Int>()
                for (i in start .. end) {
                    counter[s[i]] = counter.getOrDefault(s[i], 0) + 1
                }

                val maxCount = counter.values.maxOrNull() ?: 0
                if ((end - start + 1) - maxCount <= k) {
                    result = max(result, end - start + 1)
                }
            }
        }

        return result
    }

    /**
     * TC: O(n), SC: O(1)
     */
    private fun usingSlidingWindow(s: String, k: Int): Int {
        var (maxLength, start) = 0 to 0
        val count = IntArray(26)

        for (end in s.indices) {
            count[s[end] - 'A']++
            while (end - start + 1 - count.max() > k) {
                count[s[start] - 'A']--
                start++
            }
            maxLength = max(end - start + 1, maxLength)
        }

        return maxLength
    }

    @Test
    fun `문자열이 주어졌을 때 동일한 문자를 포함하는 가장 긴 부분 문자열의 길이를 반환한다 문자는 최대 k번 변경할 수 있다`() {
        characterReplacement("ABAB", 2) shouldBe 4
        characterReplacement("AABAB", 2) shouldBe 5
        characterReplacement("AABAB", 1) shouldBe 4
        characterReplacement("AABBAB", 1) shouldBe 4
    }
}

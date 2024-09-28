package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test
import kotlin.math.max

class `longest-substring-without-repeating-characters` {

    fun lengthOfLongestSubstring(s: String): Int {
        if (s.length <= 1) return s.length
        return usingSet(s)
    }

    /**
     * 1. 사용한 문자를 Set에 저장하여 확인하고, 중복된다면 해당 문자의 위치까지 모든 문자를 제거한다.
     * TC: O(n), SC: O(n)
     */
    private fun usingSet(s: String): Int {
        var left = 0
        val used = mutableSetOf<Char>()
        var maxLength = 0

        for (right in s.indices) {
            if (!used.contains(s[right])) {
                maxLength = max(right - left + 1, maxLength)
                used.add(s[right])
            } else {
                while (used.contains(s[right])) {
                    used.remove(s[left])
                    left++
                }
                used.add(s[right])
            }
        }

        return maxLength
    }

    @Test
    fun `입력받은 문자열의 반복되는 문자가 없는 가장 긴 부분 문자열의 길이를 반환한다`() {
        lengthOfLongestSubstring("ababc") shouldBe 3
        lengthOfLongestSubstring("bbbbb") shouldBe 1
        lengthOfLongestSubstring("abcabcbb") shouldBe 3
        lengthOfLongestSubstring("pwwkew") shouldBe 3
    }
}

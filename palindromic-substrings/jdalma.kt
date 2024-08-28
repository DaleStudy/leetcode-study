package leetcode_study

import io.kotest.matchers.equals.shouldBeEqual
import org.junit.jupiter.api.Test

class `palindromic-substrings` {

    fun countSubstrings(s: String): Int {
        return dp(s)
    }

    // 1. 브루트포스 3중 반복문
    // 시간복잡도: O(n^3), 공간복잡도: O(1)
    private fun bruteForce(s: String): Int {

        fun isPalindrome(text: String, left: Int, right: Int): Boolean {
            var (start, end) = left to right
            while (start < end) {
                if (text[start] != text[end]) {
                    return false
                }
                start++
                end--
            }
            return true
        }

        var count = 0
        s.indices.forEachIndexed { left, _ ->
            (left until s.length).forEach { right ->
                if (isPalindrome(s, left, right)) {
                    count++
                }
            }
        }
        return count
    }

    // 2. 문자열의 길이가 홀수,짝수를 감안하여 특정 지점부터 두 개의 포인터 left , right를 비교한다.
    // 시간복잡도: O(n^2), 공간복잡도: O(1)
    private fun twoPointer(s: String): Int {

        fun palindromeCount(text: String, left: Int, right: Int): Int {
            var count = 0
            var (l , r) = left to right
            while (l >= 0 && r < text.length && text[l--] == text[r++]) {
                count++
            }
            return count
        }

        var result = 0
        s.indices.forEachIndexed { index, e ->
            val even = palindromeCount(s, index, index + 1)
            val odd = palindromeCount(s, index - 1, index + 1)
            result += even + odd + 1
        }

        return result
    }

    // 3. DP : 이전에 비교했던 결과를 기억하여 (현재 주어진 start, end  비교) && (이전 start, end 비교)
    // 시간복잡도: O(n^2), 공간복잡도: O(n^2)
    private fun dp(s: String): Int {
        val len = s.length
        val dp = Array(len) { BooleanArray(len) { false } }

        for (end in 0 until len) {
            for (start in end downTo 0) {
                if (start == end) {
                    dp[start][end] = true
                } else if (start + 1 == end) {
                    dp[start][end] = s[start] == s[end]
                } else {
                    dp[start][end] = s[start] == s[end] && dp[start + 1][end - 1]
                }
            }
        }

        return dp.sumOf { row -> row.count { it } }
    }

    @Test
    fun `주어진 문자열의 회문인 부분 문자열의 개수를 반환한다`() {
        countSubstrings("abc") shouldBeEqual 3
        countSubstrings("aaa") shouldBeEqual 6
        countSubstrings("ababa") shouldBeEqual 9
        countSubstrings("abcda") shouldBeEqual 5
    }
}

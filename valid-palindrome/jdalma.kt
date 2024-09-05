package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

class `valid-palindrome` {

    /**
     * 입력받은 문자열의 양 끝부터 투 포인터를 이용하여 비교한다.
     * TC: O(n), SC: O(1)
     */
    fun isPalindrome(s: String): Boolean {
        var (left, right) = 0 to s.length - 1
        while (left < right) {
            while (left < right && !isAlphabetOrDigit(s[left])) {
                left++
            }
            while (left < right && !isAlphabetOrDigit(s[right])) {
                right--
            }
            if (s[left].lowercaseChar() != s[right].lowercaseChar()) {
                return false
            }
            left++
            right--
        }
        return true
    }

    private fun isAlphabetOrDigit(c: Char): Boolean = c.isDigit() || (c in 'a' .. 'z') || (c in 'A' .. 'Z')

    @Test
    fun `입력받은 문자열의 영숫자가 팰린드롬 여부를 반환한다`() {
        isPalindrome("A man, a plan, a canal: Panama") shouldBe true
        isPalindrome("race a car") shouldBe false
        isPalindrome("ㅁaㄹㅁb듐노+_c$#&$%#b*&@!!@a$") shouldBe true
    }

    @Test
    fun `입력받은 문자열이 공백만 존재한다면 참을 반환한다`() {
        isPalindrome(" ") shouldBe true
        isPalindrome("      ") shouldBe true
    }
}

package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test
import java.util.Deque
import java.util.ArrayDeque

class `valid-parentheses` {

    /**
     * 괄호의 쌍을 Stack을 활용하여 검증한다.
     * TC: O(n), SC: O(n)
     */
    fun isValid(s: String): Boolean {
        if (s.length % 2 != 0) return false
        val parentheses = mapOf(
            '(' to ')',
            '{' to '}',
            '[' to ']'
        )

        val stack: Deque<Char> = ArrayDeque()
        for (char in s) {
            if (parentheses.containsKey(char)) {
                stack.push(char)
            } else if (stack.isEmpty() || parentheses[stack.pop()] != char){
                return false
            }
        }
        return stack.isEmpty()
    }

    @Test
    fun `입력한 문자열의 괄호의 열림과 닫힘을 검증한다`() {
        isValid("()") shouldBe true
        isValid("{()}") shouldBe true
        isValid("(){}[]") shouldBe true

        isValid("{(}") shouldBe false
        isValid("){") shouldBe false
    }
}

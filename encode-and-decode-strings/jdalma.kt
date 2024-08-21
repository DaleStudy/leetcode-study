package leetcode_study

import io.kotest.matchers.equals.shouldBeEqual
import org.junit.jupiter.api.Test

/**
 * 인코딩과 디코딩을 해결할 때 구분자를 256개의 ASCII 문자 중 하나를 사용해야한다면 아래와 같은 방법을 사용할 수 있다.
 * 시간복잡도: O(n), 공간복잡도: O(1)
 */
class `encode-and-decode-strings` {

    private val DELIMITER = ":"

    fun encode(strings: List<String>): String {
        return strings.joinToString(separator = "") { e -> "${e.length}$DELIMITER$e" }
    }

    fun decode(string: String): List<String> {
        var index = 0
        val result = mutableListOf<String>()
        while (index < string.length) {
            val delimiterIndex = string.indexOf(DELIMITER, startIndex = index)
            val size = string.substring(index, delimiterIndex).toInt()
            result.add(string.substring(delimiterIndex + 1, delimiterIndex + size + 1))
            index = delimiterIndex + size + 1
        }
        return result
    }

    @Test
    fun `문자열 목록을 하나의 문자열로 인코딩한다`() {
        encode(listOf("leet","co:de","l:o:v:e","you")) shouldBeEqual "4:leet5:co:de7:l:o:v:e3:you"
    }

    @Test
    fun `문자열을 문자열 목록으로 디코딩한다`() {
        decode("4:leet5:co:de7:l:o:v:e3:you") shouldBeEqual listOf("leet","co:de","l:o:v:e","you")
    }
}

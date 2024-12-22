package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

/**
 * Leetcode
 * 91. Decode Ways
 * Medium
 *
 * idea:
 * Dynamic Programming
 * 숫자는 최소 한 자리에서 최대 두자리까지 해석될 수 있는 여지가 있다.
 * 따라서 "1111"이라는 문자열이 가질 수 있는 Decoding 경우의 수는 다음 두 가지가 될 수 있다.
 *   - "111"이 가지는 Decoding 경우의수 + "1"
 *   - "11"이 가지는 Decoding 경우의 수 + "11"
 * Note.
 * "0"이 가지는 Decoding 경우의 수는 없다는 것.
 * "1"부터 "26"까지만 디코딩 가능한 것.
 */
class DecodeWays {
    /**
     * Runtime: 17 ms(Beats: 11.98 %)
     * Time Complexity: O(n)
     *
     * Memory: 38.81 MB(Beats: 6.08 %)
     * Space Complexity: O(n)
     *   - s의 길이만큼의 DP 배열(dp) 필요
     */
    fun numDecodings(s: String): Int {
        val dp = IntArray(s.length)

        // 초기항: dp[0]
        dp[0] = if (s[0] == '0') 0 else 1
        if (s.length == 1) return dp[0]

        // 초기항: dp[1]
        val oneDigit = dp[0] * (if (s[1] == '0') 0 else 1)
        val twoDigitNumber = (s[0] - '0') * 10 + (s[1] - '0')
        val twoDigit = if (twoDigitNumber < 10 || 26 < twoDigitNumber) 0 else 1
        dp[1] = oneDigit + twoDigit

        if (s.length == 2) return dp[1]

        // 나머지 항 계산
        for (i in 2 until s.length) {
            // 한 자리 숫자로 해석하는 경우
            val oneDigit = dp[i - 1] * (if (s[i] == '0') 0 else 1)

            // 두 자리 숫자로 해석하는 경우
            val twoDigitNumber = (s[i - 1] - '0') * 10 + (s[i] - '0')
            val twoDigit = dp[i - 2] * (if (twoDigitNumber < 10 || 26 < twoDigitNumber) 0 else 1)

            dp[i] = oneDigit + twoDigit
        }

        return dp[dp.lastIndex]
    }

    /**
     * early return, 범위 연산자, 메서드를 활용하여 가독성 개선하기
     */
    fun numDecodings2(s: String): Int {
        if (s[0] == '0') return 0
        if (s.length == 1) return 1

        val dp = IntArray(s.length)
        // 초기항: dp[0]
        dp[0] = 1

        // 초기항: dp[1]
        val oneDigit = dp[0] * (if (s[1] == '0') 0 else 1)
        val twoDigitNumber = (s[0] - '0') * 10 + (s[1] - '0')
        val twoDigit = if (twoDigitNumber in 10..26) 1 else 0
        dp[1] = oneDigit + twoDigit

        if (s.length == 2) return dp[1]

        // 나머지 항 계산
        for (i in 2 until s.length) {
            // 한 자리 숫자로 해석하는 경우
            if (s[i] != '0') {
                dp[i] += dp[i - 1]
            }

            // 두 자리 숫자로 해석하는 경우
            val twoDigitNumber = (s[i - 1] - '0') * 10 + (s[i] - '0')
            if (twoDigitNumber in 10..26) {
                dp[i] += dp[i - 2]
            }
        }

        return dp.last()
    }

    @Test
    fun test() {
        numDecodings("12") shouldBe 2
        numDecodings("226") shouldBe 3
        numDecodings("06") shouldBe 0
        numDecodings("2101") shouldBe 1
    }
}
/**
 * 개선할 점:
 *   1) 공간복잡도 O(1)로 개선
 *      배열을 만들지 않고 "전의 경우의 수"와 "전전의 경우의 수"를 변수화하면 공간 복잡도가 O(1)로 감소될 수 있습니다.
 *   2) 연산 수 줄이기
 *      다른 빠른 풀이(1ms)를 보니 두 자리 숫자로 해석하는 경우에 숫자로 변환하지 않고 character만 비교해서
 *      (s[i] == '1' || s[i] == '2' && s[i + 1] < '7') 10 <= x <= 26 인지 확인함. 이 경우 더 적은 연산을 수행.
 */

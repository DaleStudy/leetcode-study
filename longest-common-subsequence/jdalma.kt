package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test
import kotlin.math.max

class `longest-common-subsequence` {

    fun longestCommonSubsequence(text1: String, text2: String): Int {
        return usingDP(text1, text2)
    }

    /**
     * TC: O(2^(n + m)), SC: O(n + m) 시간초과!!!
     */
    private fun usingBruteForce(text1: String, text2: String): Int {

        fun dfs(i: Int, j: Int): Int =
            if (i == text1.length || j == text2.length) 0
            else if(text1[i] == text2[j]) 1 + dfs(i + 1, j + 1)
            else max(dfs(i + 1, j), dfs(i, j + 1))

        return dfs(0, 0)
    }

    /**
     * TC: O(n * m), SC: O(n * m)
     */
    private fun usingMemoization(text1: String, text2: String): Int {

        fun dfs(i: Int, j: Int, memo: Array<IntArray>): Int {
            if (i == text1.length || j == text2.length) return 0
            else if (memo[i][j] != -1) return memo[i][j]

            memo[i][j] = if(text1[i] == text2[j]) 1 + dfs(i + 1, j + 1, memo)
            else max(dfs(i + 1, j, memo), dfs(i, j + 1, memo))

            return memo[i][j]
        }
        val memo = Array(text1.length) { IntArray(text2.length) { -1 } }
        return dfs(0, 0, memo)
    }

    /**
     * TC: O(n * m), SC: O(n * m)
     */
    private fun usingDP(text1: String, text2: String): Int {
        val dp = Array(text1.length + 1) { IntArray(text2.length + 1) }
        for (i in text1.indices) {
            for (j in text2.indices) {
                dp[i + 1][j + 1] = if (text1[i] == text2[j]) dp[i][j] + 1
                else max(dp[i + 1][j], dp[i][j + 1])
            }
        }
        return dp[text1.length][text2.length]
    }

    @Test
    fun `입력받은 두 문자열의 가장 긴 공통 부분 수열의 길이를 반환하라`() {
        longestCommonSubsequence("abcde", "ace") shouldBe 3
        longestCommonSubsequence("abc", "abc") shouldBe 3
        longestCommonSubsequence("abcdefghi", "defi") shouldBe 4
        longestCommonSubsequence("abc", "def") shouldBe 0
    }
}

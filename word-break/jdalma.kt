package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

class `word-break` {

    fun wordBreak(s: String, wordDict: List<String>): Boolean {
        return usingDP(s, wordDict)
    }

    /**
     * 1. DFS 사용 (시간초과)
     * TC: O(w^s * wordDict 단어의 길이), SC: O(s)
     */
    private fun usingDFS(s: String, wordDict: List<String>): Boolean {

        fun recursion(s: String, wordDict: List<String>, index: Int): Boolean =
            if (index == s.length) true
            else {
                wordDict.map { word ->
                    var result = false
                    if (index + word.length < s.length + 1 && s.substring(index, index + word.length) == word) {
                        result = recursion(s, wordDict, index + word.length)
                    }
                    result
                }.find { it } ?: false
            }

        return recursion(s, wordDict, 0)
    }

    /**
     * 2, 사전에 담겨있는 문자열들을 기준으로 인덱스를 증가시키면서 문자열을 완성시킨다. 한 번 탐색하여 문자열을 완성시키지 못한 인덱스를 저장하여 해당 인덱스는 다시 탐색하지 않도록 하여 성능을 개선한다.
     * TC: O(s * w * wordDict 단어의 길이), SC: O(s)
     */
    private fun usingMemoizationDFS(s: String, wordDict: List<String>): Boolean{

        fun dfs(s: String, wordDict: List<String>, index: Int, memo: MutableSet<Int>): Boolean {
            val len = s.length
            if(index == len) return true
            else if(memo.contains(index)) return false

            for (word in wordDict) {
                if (index + word.length < s.length + 1 &&
                    s.substring(index, index + word.length) == word &&
                    dfs(s, wordDict, index + word.length, memo)) {
                    return true
                }
            }
            memo.add(index)
            return false
        }

        if(s.isEmpty()) return false
        return dfs(s, wordDict, 0, mutableSetOf())
    }

    /**
     * 3. 문자열의 끝부터 0까지 순회하면서 순회하는 범위의 문자열을 만들 수 있다면 해당 인덱스를 true로 변환하여 이전에 사용한 연산의 결과를 재활용한다.
     * TC: O(s * w * wordDict 단어의 길이) SC: O(s)
     */
    private fun usingDP(s: String, wordDict: List<String>): Boolean {
        val dp = BooleanArray(s.length + 1).apply {
            this[s.length] = true
        }

        for (index in s.length - 1 downTo 0) {
            for (word in wordDict) {
                if (dp[index]) break
                else if (index + word.length <= s.length && s.substring(index, index + word.length) == word) {
                    dp[index] = dp[index + word.length]
                }
            }
        }
        return dp[0]
    }

    @Test
    fun `문자열과 문자열 사전이 주어졌을 때 문자열 사전을 이용하여 문자열을 완성할 수 있으면 참을 반환한다`() {
        wordBreak("applepenapple", listOf("apple", "pen")) shouldBe true
        wordBreak("leetcode", listOf("leet", "co", "de")) shouldBe true
        wordBreak("abcd", listOf("a","abc","b","cd")) shouldBe true
        wordBreak("cars", listOf("car","ca","rs")) shouldBe true
    }

    @Test
    fun `문자열과 문자열 사전이 주어졌을 때 문자열 사전을 이용하여 문자열을 완성할 수 없다면 거짓을 반환한다`() {
        wordBreak("catsandog", listOf("cats", "dog", "sand", "and", "cat")) shouldBe false
    }
}

class Solution {
    /**
     * 시간 : O(s^2*w), 공간 : O(s)
     * */
    fun wordBreak(s: String, wordDict: List<String>): Boolean {
        val dp = BooleanArray(s.length + 1)
        dp[0] = true
        for (i in 1..s.length) {
            val subS = s.substring(0, i)
            val endWord = wordDict.firstOrNull { subS.endsWith(it) }
            if (endWord != null) {
                dp[i] = dp[i - endWord.length]
            }
        }
        return dp[s.length]
    }
}

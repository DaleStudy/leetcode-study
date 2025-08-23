object Solution {
    def wordBreak(s: String, wordDict: List[String]): Boolean = {
        val dp = Array.fill(s.length + 1)(false) // S(s, wordDict, word) = O(s.length)
        dp(0) = true
        for (i <- 1 to s.length) {
            for (word <- wordDict) {
                if (i >= word.length && dp(i - word.length) && s.substring(i - word.length, i) == word) {
                    dp(i) = true // T(s, wordDict, word) = O(s.length * wordDict.length * word.length)
                }
            }
        }
        dp(s.length)
    }
}

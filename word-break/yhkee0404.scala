object Solution {
    def wordBreak(s: String, wordDict: List[String]): Boolean = {
        val dp = Array.fill(s.length + 1)(false) // S(s, wordDict, word) = O(s.length)
        dp(0) = true
        (0 to s.length - 1).exists { i =>
            if (! dp(i)) false
            else {
                for (word <- wordDict if ! dp(s.length)) {
                    val j = i + word.length
                    if (j <= s.length && ! dp(j) && s.substring(i, j) == word) {
                        dp(j) = true // T(s, wordDict, word) = O(s.length * wordDict.length * word.length)
                    }
                }
                dp(s.length)
            }
        }
    }
}

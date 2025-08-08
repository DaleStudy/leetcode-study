class Solution {
    fun numDecodings(s: String): Int {
        if (s.isEmpty() || s[0] == '0') return 0

        val n = s.length
        val dp = IntArray(n + 1)

        dp[0] = 1
        dp[1] = 1

        for (i in 2..n) {
            val currentChar = s[i - 1]
            val prevChar = s[i - 2]

            if (currentChar != '0') {
                dp[i] += dp[i - 1]
            }

            val twoDigit = (prevChar - '0') * 10 + (currentChar - '0')
            if (twoDigit in 10..26) {
                dp[i] += dp[i - 2]
            }
        }

        return dp[n]
    }
}

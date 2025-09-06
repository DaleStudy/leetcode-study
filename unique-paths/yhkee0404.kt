class Solution {
    fun uniquePaths(m: Int, n: Int): Int {
        val dp = List(m + 1) {MutableList(n + 1) {0}}
        dp[0][1] = 1
        for (i in 1..m) {
            for (j in 1..n) {
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
            }
        }
        return dp.last().last()
    }
}

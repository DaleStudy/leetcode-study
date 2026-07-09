class Solution {
    fun climbStairs(n: Int): Int {
        if (n == 1) return 1
        if (n == 2) return 2

        val dp = IntArray(n + 1) { 0 }
        dp[1] = 1
        dp[2] = 2

        for (i in 3 .. n) {
            dp[i] = dp[i - 1] + dp[i - 2]
        }

        return dp[n]
    }
}

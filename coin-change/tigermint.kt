class Solution {
    fun coinChange(coins: IntArray, amount: Int): Int {
        val dp = IntArray(amount + 1) { amount + 1 }
        dp[0] = 0

        for (i in 1..amount) {
            for (c in coins) {
                if (i - c >= 0) {
                    dp[i] = minOf(dp[i], dp[i - c] + 1)
                }
            }
        }

        return if (dp[amount] > amount) - 1 else dp[amount]
    }
}

/**
 * 시간복잡도: O(amount × coins.length)
 * 공간복잡도: O(amount)
 */

class Solution {
    fun coinChange(coins: IntArray, amount: Int): Int {
        val dp = IntArray(amount + 1) { Int.MAX_VALUE }
        dp[0] = 0

        for (i in 1..amount) {
            for (coin in coins) {
                if (i - coin >= 0 && dp[i - coin] != Int.MAX_VALUE) {
                    dp[i] = minOf(dp[i], dp[i - coin] + 1)
                }
            }
        }

        return if (dp[amount] == Int.MAX_VALUE) -1 else dp[amount]
    }
}

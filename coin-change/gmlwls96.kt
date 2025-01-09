class Solution {
    // 알고리즘 : dp
    /** 풀이
     * dp배열에 최소한의 동전의 개수를 저장.
     * dp[i] = min(dp[i - 동전값], dp[i]) 중 더 작은값이 최소 동전의 개수.
     * */
    // 시간 : O(coins.len*amount), 공간 : O(amount)
    fun coinChange(coins: IntArray, amount: Int): Int {
        val initValue = Int.MAX_VALUE / 2
        val dp = IntArray(amount + 1) { initValue }
        dp[0] = 0
        for (i in 1..amount) {
            coins.forEach { c ->
                if (c <= i) {
                    dp[i] = min(dp[i - c] + 1, dp[i])
                }
            }
        }
        return if (dp[amount] == initValue) {
            -1
        } else {
            dp[amount]
        }
    }
}

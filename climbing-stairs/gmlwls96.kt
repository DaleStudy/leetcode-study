class Solution {
    // 시간복잡도 : O(n)
    fun climbStairs(n: Int): Int {
        val dp = IntArray(n+1)
        dp[1] = 1
        dp[2] = 2
        for(i in 3..n){ // 3부터 n까지 for문.
            dp[i] = dp[i-1] + dp[i-2]
        }
        return dp[n]
    }
}

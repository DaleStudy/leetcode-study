object Solution {
    def climbStairs(n: Int): Int = {
        val dp = Array.ofDim[Int](n + 1)
        dp(0) = 1
        dp(1) = 1
        for (i <- 2 to n) {
            dp(i) = dp(i - 1) + dp(i - 2)
        }
        dp(n)
    }
}

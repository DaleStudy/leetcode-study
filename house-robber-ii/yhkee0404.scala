object Solution {
    def rob(nums: Array[Int]): Int = {
        if (nums.length == 1) {
            return nums(0)
        }
        val dp = Array.fill(nums.length)(Array.fill(2)(0)) // T(n) = S(n) = O(n)
        dp(0)(1) = nums(0)
        dp(1)(0) = nums(1)
        dp(1)(1) = nums(0)
        for (i <- 2 until nums.length) {
            for (j <- 0 to 1) {
                dp(i)(j) = Math.max(dp(i - 1)(j), dp(i - 2)(j) + nums(i))
            }
        }
        Math.max(dp(nums.length - 2)(1), dp(nums.length - 1)(0))
    }
}

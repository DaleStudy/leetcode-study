package leetcode_study

/*
* 주어진 숫자 배열에서 Subarray가 가장 큰 수를 구하는 문제
* 시간 복잡도: O(n)
* -> 주어진 배열만큼 계산
* 공간 복잡도: O(n)
* -> 가중치를 더하는 배열 필요
* */
fun maxSubArray(nums: IntArray): Int {
    val dp = IntArray(nums.size)
    dp[0] = nums[0]

    for (i in 1 until nums.size) {
        if (dp[i - 1] + nums[i] >= 0 && dp[i-1] >= 0) {
            dp[i] = dp[i - 1] + nums[i]
        } else {
            dp[i] = nums[i]
        }
    }
    return dp.max()
}

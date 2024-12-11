package leetcode_study

/**
 * DP를 사용한 문제 풀이.
 * DP를 사용하지 않고 모든 경우의 수를 계산하여 최대 값을 구하려면 100!에 해당하는 연산이 필요하며, 이는 시간 초과를 초래합니다.
 * 시간 복잡도 : O(n)
 * -> 주어진 숫자 배열 만큼 반복 진행
 * 공간 복잡도 : O(n)
 * -> 숫자 배열만큼의 가중치를 담을 배열 필요
 */
fun rob(nums: IntArray): Int {
    val dp = IntArray(nums.size)

    if (nums.size == 1) {
        return nums[0]
    }

    if (nums.size == 2) {
        return max(nums[0], nums[1])
    }

    dp[0] = nums[0]
    dp[1] = nums[1]
    dp[2] = nums[2] + dp[0]

    for (i in 3 until nums.size) {
        dp[i] = max(dp[i-3], dp[i-2]) + nums[i]
    }
    return dp.max()
}

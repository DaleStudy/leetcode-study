class Solution {
    // 배열에서 인접한 항은 접근할 수 없을 때, 인접하지 않은 항을 더해 가장 큰 값을 구하는 문제
    // 1. DP를 사용해 각 집마다 선택하거나 건너뛰는 경우를 누적 계산
    // 2. 현재 집을 털 때, 이전 집을 털지 않은 경우만 더할 수 있게끔 계산
    fun rob(nums: IntArray): Int {
        if (nums.isEmpty()) return 0
        var prev1 = 0  // 바로 이전 집까지의 최대 이익
        var prev2 = 0  // 이전 이전 집까지의 최대 이익

        for (num in nums) {
            var temp = prev1
            prev1 = maxOf(prev2 + num, prev1)
            prev2 = temp
        }

        return prev1
    }
}
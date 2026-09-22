/**
 * TC: O(n)
 * SC: O(1)
 * 음수가 있기 때문에 현 시점에 min/max 모두 추적해야한다
 */
class Solution {
    fun maxProduct(nums: IntArray): Int {
        var curMax = nums[0]
        var curMin = nums[0]
        var answer = nums[0]

        for (i in 1 ..< nums.size) {
            val n = nums[i]

            val nextMax = maxOf(n, curMax * n, curMin * n)
            val nextMin = minOf(n, curMax * n, curMin * n)

            curMax = nextMax
            curMin = nextMin
            answer = maxOf(answer, curMax)
        }
        return answer
    }
}

import kotlin.math.max

class Solution {
    fun rob(nums: IntArray): Int {
        var prevMaxMoney = 0
        var maxMoney = 0
        for (money in nums) {
            prevMaxMoney.let {
                prevMaxMoney = maxMoney
                maxMoney = max(it + money, maxMoney)
            }
        }
        return maxMoney
    }
}

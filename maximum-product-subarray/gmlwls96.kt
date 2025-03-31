class Solution {
    fun maxProduct(nums: IntArray): Int {
        var max = 1
        var min = 1
        var result = nums[0]
        nums.forEach { num ->
            val v1 = min * num
            val v2 = max * num
            min = min(min(v1, v2), num)
            max = max(max(v1, v2), num)
            result = max(max, result)
        }
        return result
    }
}

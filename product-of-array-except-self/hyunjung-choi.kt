class Solution {
    fun productExceptSelf(nums: IntArray): IntArray =
        IntArray(nums.size) { 1 }.apply {
            var leftProduct = 1
            for (i in 1 until nums.size) {
                leftProduct *= nums[i - 1]
                this[i] = leftProduct
            }

            var rightProduct = 1
            for (i in nums.size - 2 downTo 0) {
                rightProduct *= nums[i + 1]
                this[i] *= rightProduct
            }
        }
}
